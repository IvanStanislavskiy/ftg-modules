from .. import loader, utils
from telethon import events
from asyncio import sleep

class FrogMod(loader.Module):
    """Клоун пон."""
    strings = {'name': 'Kjabik'}

    async def watcher(self, message, event):
        try:
            me = await message.client.get_me()
            name = me.first_name

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
                                await sleep(20)
                                await message.client.send_message(chat, 'жаба инфо')
                                response = await response

                                if "🍭:Можно покормить" in response.text:
                                    args = [int(x) for x in response.text.split() if x.isnumeric()]
                                    randelta = random.randint(20, 60)
                                    if len(args) == 4: delta = timedelta(hours=args[0], minutes=args[1], seconds=randelta)

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
                            except:
                                pass
