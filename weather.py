import requests
from .. import loader, utils


def register(cb):
    cb(WeatherMod())
    
class WeatherMod(loader.Module):
    """Погода с сайта wttr.in"""
    strings = {'name': 'Weather'}
    
    async def pwcmd(self, message):
        """"Кидает погоду картинкой.\nИспользование: .pw <city>; ничего."""
        args = utils.get_args_raw(message).replace(' ', '+')
        await message.edit("Wait...")
        city = requests.get(f"https://wttr.in/{args if args != None else ''}.png").content
        await message.client.send_file(message.to_id, city)
        await message.delete()


    async def awcmd(self, message):
        """Кидает погоду ascii-артом.\nИспользование: .aw <city>; ничего."""
        city = utils.get_args_raw(message)
        await message.edit("Wait...")
        r = requests.get(f"https://wttr.in/{city if city != None else ''}?0?q?T&lang=ru")
        await message.edit(f"<code>Город: {r.text}</code>")
