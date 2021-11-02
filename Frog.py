import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message
from telethon import events
from asyncio import sleep

@loader.tds
class FroggMod(loader.Module):
    """helpmv"""
    strings = {'name': 'Jabik'}

    async def watcher(self, message):
        chat = message.chat_id
        me = await message.client.get_me()
        name = me.first_name
        randelta = random.randint(30, 45)
        EK = {-1001363387233, -519750908}
        PI = {1501652358, 1744359315}

        if message.sender_id in {1568736811}:
            if "Моя жаба" in message.message:
                async with message.client.conversation(chat) as conv:
                    response = conv.wait_event(events.NewMessage(incoming=True, from_users=PI, chats=message.chat_id))
                    await sleep(3)
                    await message.client.send_message(chat, 'жаба инфо')
                    response = await response

                    if "(Можно откормить)" in response.text:
                        if message.chat_id in EK:
                            delta = timedelta(hours=4, seconds=randelta)
                            delta_r = timedelta(hours=4, seconds=50)
                            await sleep(3)
                            await message.respond('откормить жабу')
                            await message.client.send_message(chat, 'откормить жабу', schedule=delta)
                            await message.client.send_message(chat, 'Моя жаба', schedule=delta_r)
                        else:
                            if "Жабу можно покормить" in response.text:
                                delta = timedelta(hours=12, seconds=randelta)
                                delta_r = timedelta(hours=12, seconds=50)
                                await sleep(3)
                                await message.respond('покормить жабу')
                                await message.client.send_message(chat, 'Покормить жабу', schedule=delta)
                                await message.client.send_message(chat, 'Моя жаба', schedule=delta_r)

                    if "Отправить на" in response.text:
                        if "Можно отправиться" in response.text:
                            if message.chat_id in {-1001363387233}:
                                await sleep(3)
                                await message.respond('реанимировать жабу')
                                await sleep(3)
                                await message.respond('отправиться в золотое подземелье')
                                response = conv.wait_event(events.NewMessage(incoming=True, from_users=PI, chats=message.chat_id))
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

                    if "Жабу можно отправить" in response.text:
                        delta = timedelta(hours=2, seconds=randelta)
                        delta_r = timedelta(hours=2, seconds=50)
                        if message.chat_id in {-1001441941681}:
                            if "В подземелье можно через 2ч" in response.text:
                                await sleep(3)
                                await message.respond('реанимировать жабу')
                                await sleep(3)
                                await message.respond('работа крупье')
                                await message.client.send_message(chat, 'Завершить работу', schedule=delta)
                                await message.client.send_message(chat, 'Моя жаба', schedule=delta_r)
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

        if "Коля напади" in message.message:
            await sleep(1)
            await message.respond('реанимировать жабу')
            await sleep(1)
            await message.reply('напасть на клан')
        if "Коля подземелье" in message.message:
            await sleep(1)
            await message.respond('реанимировать жабу')
            await sleep(1)
            await message.reply('отправиться в золотое подземелье')
