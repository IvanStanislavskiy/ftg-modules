import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message
from asyncio import sleep

@loader.tds
class FrogFarmMod(loader.Module):
    """Хатьфу."""
    strings = {'name': 'jaba'}

    async def watcher(self, message):
        try:
            if message.chat_id in {-1001363387233}:
                if message.sender_id in {1124824021}:
                    if "Йоу" in message.message:
                        chat = message.chat_id
                        async with message.client.conversation(chat) as conv:
                            try:
                                response = conv.wait_event(
                                    events.NewMessage(
                                        incoming=True,
                                        from_users=message.sender_id,
                                        chats=message.chat_id,))
                                await sleep(1)
                                await message.client.send_message(chat, 'жаба инфо')
                                response = await response

                                if "🍭:Можно покормить" in response.text:
                                    args = [int(x) for x in response.text if x.isnumeric()]
                                    randelta = random.randint(20, 60)
                                    if len(args) == 4: delta = timedelta(hours=args[0], minutes=args[1], seconds=randelta)


                                if "(Можно откормить)" in response.text:
                                    await sleep(10)
                                    await message.respond('откормить жабу')
                                if "🏃‍♂️:Можно забрать" in response.text:
                                    await sleep(10)
                                    await message.respond('завершить работу')
                                    if "☠️:Можно отправиться" in response.text:
                                        await sleep(10)
                                        await message.respond('реанимировать жабу')
                                        await sleep(10)
                                        await message.respond('отправиться в золотое подземелье')
                                elif "🏃‍♂️:Отправить на работу" in response.text:
                                    if "☠️:Можно отправиться" in response.text:
                                        await sleep(10)
                                        await message.respond('реанимировать жабу')
                                        await sleep(10)
                                        await message.respond('отправиться в золотое подземелье')
                                elif "🏃‍♂️:Жабу можно" in response.text:
                                    if "☠️:Можно отправиться" in response.text:
                                        await sleep(10)
                                        await message.respond('реанимировать жабу')
                                        await sleep(10)
                                        await message.respond('отправиться в золотое подземелье')
                                    elif ("☠️:В подземелье можно через 2ч" in response.text):
                                        await sleep(10)
                                        await message.respond('реанимировать жабу')
                                        await sleep(10)
                                        await message.respond('работа грабитель')
                                    else:
                                        pass
                                else:
                                    pass
                            except:
                                pass

                if "Ваня напади" in message.message:
                    await message.reply('напасть на клан')
                if "Ваня подземелье" in message.message:
                    await message.reply('отправиться в золотое подземелье')
                if "К вам заглянул пчеловод!" in message.message:
                    await message.reply('@ffugglyy')
                if "Бзззз! С пасеки сбежали пчёлы! Ловите их!" in message.message:
                    await message.reply('@ffugglyy')
                if "Вы успешно покормили жабу!" in message.message:
                    await message.reply('откормить жабу')
                if "Ваня турнир" in message.message:
                    await message.reply('начать турнирное сражение')

            if message.sender_id in {1682801197}:
                if "Жабу на тусу" in message.message:
                    await message.respond('жабу на тусу')
                if "Клан вознаграждение" in message.message:
                    await message.respond('клан вознаграждение')
        except: pass
