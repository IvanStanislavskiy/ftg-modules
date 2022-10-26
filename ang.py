
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineKeyboardButton,
    InputTextMessageContent,
)
from asyncio import sleep
from telethon.tl.types import Message
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.utils import get_display_name
from .. import loader  # noqa
import logging
from ..inline import GeekInlineQuery, rand  # noqa
from .. import utils  # noqa

logger = logging.getLogger(__name__)

ua = [
    "был 🔇 обеззвучен"
]


class AirAlertMod(loader.Module):
    """🇺🇦 Предупреждение о воздушной тревоге.
    Нужно быть подписаным на @air_alert_ua и включены уведомления в вашем боте"""

    strings = {"name": "AirAlert", "author": "morisummermods"}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
        self.regions = db.get(self.strings["name"], "regions", [])
        self.bot_id = (await self.inline.bot.get_me()).id
        self.nametag = db.get(self.strings["name"], "nametag", "")
        self.forwards = db.get(self.strings["name"], "forwards", [])
        self.me = (await client.get_me()).id
        try:
            await client(
                JoinChannelRequest(await self.client.get_entity("t.me/air_alert_ua"))
            )
        except Exception:
            logger.error("Can't join t.me/air_alert_ua")
        try:
            channel = await self.client.get_entity(f"t.me/{self.strings['author']}")
            await client(JoinChannelRequest(channel))
        except Exception:
            logger.error(f"Can't join {self.strings['author']}")
        try:
            post = (await client.get_messages(self.strings["author"], ids=[15]))[0]
            await post.react("❤️")
        except Exception:
            logger.error(f"Can't react to t.me/{self.strings['author']}")

    async def alertforwardcmd(self, message: Message) -> None:
        """Перенаправление предупреждений в другие чаты.
        Для добавления/удаления введите команду с ссылкой на чат.
        Для просмотра чатов введите команду без аргументов
        Для установки кастомной таблички введите .alertforward set <text>"""
        text = utils.get_args_raw(message)
        if text[:3] == "set":
            self.nametag = text[4:]
            self.db.set(self.strings["name"], "nametag", self.nametag)
            return await utils.answer(
                message,
                f"🏷 <b>Табличка успешно установлена: <code>{self.nametag}</code></b>",
            )
        if not text:
            chats = "<b>Текущие чаты для перенаправления: </b>\n"
            for chat in self.forwards:
                chats += f"{get_display_name(await self.client.get_entity(chat))}\n"
            await utils.answer(message, chats)
            return
        try:
            chat = (await self.client.get_entity(text.replace("https://", ""))).id
        except Exception:
            await utils.answer(message, "<b>Чат не найден</b>")
            return
        if chat in self.forwards:
            self.forwards.remove(chat)
            self.db.set(self.strings["name"], "forwards", self.forwards)
            await utils.answer(message, "<b>Чат успешно удален для перенаправления</b>")
        else:
            self.forwards.append(chat)
            self.db.set(self.strings["name"], "forwards", self.forwards)
            await utils.answer(
                message, "<b>Чат успешно установлен для перенаправления</b>"
            )

    async def alert_inline_handler(self, query: GeekInlineQuery) -> None:
        """Выбор регионов.
        Чтобы получать все предупреждения введите alert all.
        Чтобы посмотреть ваши регионы alert my"""
        text = query.args
        if not text:
            result = ua
        elif text == "my":
            result = self.regions
        else:
            result = [region for region in ua if text.lower() in region.lower()]
        if not result:
            await query.e404()
            return
        res = [
            InlineQueryResultArticle(
                id=rand(20),
                title=f"{'✅' if reg in self.regions else '❌'}{reg if reg != 'all' else 'Все уведомления'}",
                description=f"Нажмите чтобы {'удалить' if reg in self.regions else 'добавить'}"
                if reg != "all"
                else f"🇺🇦 Нажмите чтобы {'выключить' if 'all' in self.regions else 'включить'} все уведомления",
                input_message_content=InputTextMessageContent(
                    f"⌛ Редактирование региона <code>{reg}</code>",
                    parse_mode="HTML",
                ),
            )
            for reg in result[:50]
        ]
        await query.answer(res, cache_time=0)

    async def watcher(self, message: Message) -> None:
        if (
                getattr(message, "out", False)
                and getattr(message, "via_bot_id", False)
                and message.via_bot_id == self.bot_id
                and "⌛ Редактирование региона" in getattr(message, "raw_text", "")
        ):
            self.regions = self.db.get(self.strings["name"], "regions", [])
            region = message.raw_text[25:]
            state = "добавлен"
            if region not in self.regions:
                self.regions.append(region)
            else:
                self.regions.remove(region)
                state = "удален"
            self.db.set(self.strings["name"], "regions", self.regions)
            try:
                e = await self.client.get_entity("t.me/air_alert_ua")
                sub = not e.left
            except Exception:
                sub = False
            n = "\n"
            res = f"<b>Регион <code>{region}</code> успешно {state}</b>{n}"
            if not sub:
                res += (
                    "<b>НЕ ВЫХОДИ С @air_alert_ua (иначе ничего работать не будет)</b>"
                )
                await self.client(
                    JoinChannelRequest(
                        await self.client.get_entity("t.me/air_alert_ua")
                    )
                )
            await self.inline.form(res, message=message)
        if (
                getattr(message, "peer_id", False)
                and getattr(message.peer_id, "chat_id", 0) == -1001387610194
                and (
                "all" in self.regions
                or any(reg in message.raw_text for reg in self.regions)
        )
        ):
            for _ in range(3):
                await self.inline.bot.send_message(
                    self.me, message.text, parse_mode="HTML"
                )
                await sleep(1)
            for chat in self.forwards:
                await self.client.send_message(
                    chat, message.text + "\n\n" + self.nametag
                )
        return
