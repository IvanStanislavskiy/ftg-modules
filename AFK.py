import time
from datetime import datetime

from telethon import types

from .. import loader, utils


@loader.tds
class AFKMod(loader.Module):
	"""Provides a message saying that you are unavailable"""
	strings = {"name": "AFK Status",
	           "gone": "<b>I'm goin' AFK</b>",
	           "back": "<b>I'm no longer AFK</b>",
	           "afk": "<b>I'm AFK right now (since {} ago).</b>",
	           "afk_reason": "<b>I'm AFK right now (since {} "
	                         "ago).\nReason:</b> <i>{}</i>"}
	def __init__(self):
		self.config = loader.ModuleConfig(
			"EXCEPTION_ID", [""], "Exceptions users IDs")
	async def client_ready(self, client, db):
		self._db = db
		self._me = await client.get_me()
	async def afkcmd(self, message):
		""".afk [message]"""
		if utils.get_args_raw(message):
			self._db.set(__name__, "afk", utils.get_args_raw(message))