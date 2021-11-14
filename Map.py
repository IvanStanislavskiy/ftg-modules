#by helpmv
import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message
from telethon import events
from asyncio import sleep

@loader.tds
class MapMod(loader.Module):
    """Frog"""
    strings = {'name': 'helpmv hello'}

    if message.sender_id in {1124824021}:
                randelta = random.randint(6, 9)
                delta = timedelta(minutes=randelta)
                if "Сейчас выбирает ход: " + name in message.message:
                    await message.click(0)
                if "Huawei 🐮 " + name in message.message:
                    await sleep (10)
                    await message.respond('реанимировать жабу')
                    await sleep (10)
                    await message.respond('отправиться за картой')
except:
       pass
