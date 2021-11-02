import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message
from telethon import events
from asyncio import sleep

@loader.tds
class FroggMod(loader.Module):
    """жаба"""
    strings = {'name': 'Jabik'}

    async def watcher(self, message):
        chat = message.chat_id
        me = await message.client.get_me()
        name = me.first_name
        randelta = random.randint(7, 9)

        if message.sender_id in {1568736811}:
            if "Моя жаба" in message.message:
                async with message.client.conversation(chat) as conv:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1501652358, chats=message.chat_id))
                    await sleep(3)
                    await message.client.send_message(chat, 'жаба инфо')
                    response = await response

                    if "(Можно откормить)" in response.text:
                        if message.chat_id in {-519750908}:
                            delta = timedelta(hours=4, seconds=randelta)
                            delta_r = timedelta(hours=4, seconds=15)
                            await sleep(3)
                            await message.respond('откормить жабу')
                            await message.client.send_message(chat, 'откормить жабу', schedule=delta)
                            await message.client.send_message(chat, 'Моя жаба', schedule=delta_r)
                        else:
                            if "Жабу можно покормить" in response.text:
                                delta = timedelta(hours=12, seconds=randelta)
                                delta_r = timedelta(hours=12, seconds=15)
                                await sleep(3)
                                await message.respond('покормить жабу')
                                await message.client.send_message(chat, 'Покормить жабу', schedule=delta)
                                await message.client.send_message(chat, 'Моя жаба', schedule=delta_r)

                    if "Можно отправиться" in response.text:
                        if message.chat_id in {-519750908}:
                            await sleep(3)
                            await message.respond('реанимировать жабу')
                            await sleep(3)
                            await message.respond('отправиться в золотое подземелье')

                    if "Жабу можно отправить" in response.text:
                        delta = timedelta(hours=2, seconds=randelta)
                        delta_r = timedelta(hours=2, seconds=15)
                        delta_k = timedelta(hours=8, seconds=randelta)
                        delta_kk = timedelta(hours=8, seconds=15)
                        if message.chat_id in {-519750908}:
                            if "В подземелье можно через 2ч" in response.text:
                                await sleep(3)
                                await message.respond('реанимировать жабу')
                                await sleep(3)
                                await message.respond('работа крупье')
                                await message.client.send_message(chat, 'Завершить работу', schedule=delta)
                                await message.client.send_message(chat, 'Моя жаба', schedule=delta_r)
                                response = conv.wait_event(events.NewMessage(incoming=True, from_users=1124824021, chats=message.chat_id))
                                await sleep (3)
                                await message.client.send_message(chat, 'мой клан')
                                response = await response
                                if "Клан" in response.text:
                                    if "🕒Пойти за картой" not in response.text:
                                        await sleep (3)
                                        await message.respond('отправиться за картой')
                                        await sleep (33)
                                        await message.respond('отправиться за картой')
                                        await message.client.send_message(chat, 'отправиться за картой', schedule=delta_k)
                                        await message.client.send_message(chat, 'отправиться за картой', schedule=delta_kk)
                        else:
                            await sleep(3)
                            await message.respond('реанимировать жабу')
                            await sleep(3)
                            await message.respond('работа крупье')
                            await message.client.send_message(chat, 'Завершить работу', schedule=delta)
                            await message.client.send_message(chat, 'Моя жаба', schedule=delta_r)


                    if "Можно забрать" in response.text:
                        delta = timedelta(hours=6, seconds=randelta)
                        delta_r = timedelta(seconds=randelta)
                        await sleep(3)
                        await message.respond('завершить работу')
                        await message.client.send_message(chat, 'поход в столовую', schedule=delta)
                        await message.client.send_message(chat, 'Моя жаба', schedule=delta_r)

        if message.sender_id in {1124824021}:
            delta = timedelta(minutes=randelta)
            if "Сейчас выбирает ход: " + name in message.message:
                await message.click(0)
            if "Господин " + name in message.message:
                await sleep (3)
                await message.respond('реанимировать жабу')
                await sleep (3)
                await message.respond('отправиться за картой')
            if "Тебе жаба, Милая Беседа" in message.message:
                await message.client.send_message(chat, 'Моя жаба', schedule=delta)
            if "позвать на тусу" in message.message:
                await sleep(3)
                await message.respond('реанимировать жабу')
                await sleep(3)
                await message.respond('жабу на тусу')

        if message.sender_id in {830605725}:
            if "Бзззз! С пасеки" in message.message:
                await message.click(0)
            if "[8🐝]" in message.message:
                await message.click(0)
            if "[4🐝]" in message.message:
                click = (await message.click(0)).message
            if "[5🟡🐝," in message.message:
                await message.click(0)
            if "[2🦠🐝," in message.message:
                await message.click(0)
            if "[5🐝, 3🔴🐝]" in message.message:
                await message.click(0)
            if "[2☢️🐝, 2🔴🐝," in message.message:
                await message.click(0)

        if message.chat_id in {-519750908}:
            if "Ваня го кв" in message.message:
                await message.respond('начать клановую войну')
            if "Ваня напади" in message.message:
                await sleep(1)
                await message.respond('реанимировать жабу')
                await sleep(1)
                await message.respond('напасть на клан')
            if "Ваня подземелье" in message.message:
                await sleep(1)
                await message.respond('реанимировать жабу')
                await sleep(1)
                await message.respond('отправиться в сереберяное подземелье')
                async with message.client.conversation(chat) as conv:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=1501652358, chats=message.chat_id))
                    await sleep (3)
                    await message.client.send_message(chat, 'мое снаряжение')
                    response = await response
                    if "🗡Ближний бой: Отсутствует" in response.text:
                        await sleep(3)
                        await message.respond('скрафтить клюв цапли')
                    if "🏹Дальний бой: Отсутствует" in response.text:
                        await sleep(3)
                        await message.respond('скрафтить букашкомет')
                    if "🐸Наголовник: Отсутствует" in response.text:
                        await sleep(3)
                        await message.respond('скрафтить наголовник из клюва цапли')
                    if "🥼Нагрудник: Отсутствует" in response.text:
                        await sleep(3)
                        await message.respond('скрафтить нагрудник из клюва цапли')
                    if "👞Налапники: Отсутствует" in response.text:
                        await sleep(3)
                        await message.respond('скрафтить налапники из клюва цапли')
                    if "🏋️‍♀️Банда: Отсутствует" in response.text:
                        await sleep(3)
                        await message.respond('собрать банду')
            if "Вы успешно покормили жабу!" in message.message:
                await message.respond('откормить жабу')
            if "Лена го за картой" in message.message:
                await message.respond('отправиться за картой')
            if "Лена инвентарь" in message.message:
                await message.respond('мой инвентарь')
            if "Лена леденцы" in message.message:
                await message.respond('использовать леденцы 3')
            if "Лена аптечки" in message.message:
                await message.reply('отправить аптечки 10')
