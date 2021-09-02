from .. import loader, utils  # pylint: disable=relative-beyond-top-level
import io
from PIL import Image, ImageOps
from telethon.tl.types import DocumentAttributeFilename
import logging
import random

logger = logging.getLogger(__name__)

def register(cb):
	cb(SpinnerMod())


@loader.tds
class SpinnerMod(loader.Module):
	"""i`m clown"""
	strings = {
		"name": "Spinner"
	}

	async def client_ready(self, client, db):
		self.client = client
	
	@loader.sudo
	async def spincmd(self, message):
		"""you spin me round..."""
		args = utils.get_args(message)
		
		if message.is_reply:
			reply_message = await message.get_reply_message()
			data = await check_media(reply_message)
			if isinstance(data, bool):
				await utils.answer(message, "<code>Реплай на пикчу или стикер</code>")
				return
		else:
			await utils.answer(message, "`Реплай на пикчу или стикер`")
			return
			
		image = io.BytesIO()
		await self.client.download_media(data, image)
		image = Image.open(image)
		image.thumbnail((512, 512), Image.ANTIALIAS)
		img = Image.new("RGB", (512, 512), "black")
		img.paste(image, ((512-image.width)//2, (512-image.height)//2))
		image = img
		way = random.choice([1, -1])
		frames = []
		for i in range(1, 60):
			im = image.rotate(i*6*way)
			frames.append(im)
		frames.remove(im)

		image_stream = io.BytesIO()
		image_stream.name = "spin.gif"
		im.save(image_stream, "GIF", save_all=True, append_images=frames, duration = 10)
		image_stream.seek(0)
		await utils.answer(message, image_stream)

	@loader.sudo
	async def epilepsycmd(self, message):
		"""ПРИВЕТ ЭПИЛЕТИКИ АХАХАХХА"""
		args = utils.get_args(message)
		
		if message.is_reply:
			reply_message = await message.get_reply_message()
			data = await check_media(reply_message)
			if isinstance(data, bool):
				await utils.answer(message, "<code>Реплай на пикчу или стикер!</code>")
				return
		else:
			await utils.answer(message, "`Реплай на пикчу или стикер блять`")
			return
			
		image = io.BytesIO()
		await self.client.download_media(data, image)
		image = Image.open(image).convert("RGB")
		invert = ImageOps.invert(image)

		image_stream = io.BytesIO()
		image_stream.name = "epilepsy.gif"
		image.save(image_stream, "GIF", save_all=True, append_images=[invert], duration = 1)
		image_stream.seek(0)
		await utils.answer(message, image_stream)

	

async def check_media(reply_message):
	if reply_message and reply_message.media:
		if reply_message.photo:
			data = reply_message.photo
		elif reply_message.document:
			if DocumentAttributeFilename(file_name='AnimatedSticker.tgs') in reply_message.media.document.attributes:
				return False
			if reply_message.gif or reply_message.video or reply_message.audio or reply_message.voice:
				return False
			data = reply_message.media.document
		else:
			return False
	else:
		return False

	if not data or data is None:
		return False
	else:
		return data