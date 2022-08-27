import json
from aiogram import types, Bot, Dispatcher
from django.http import HttpRequest, HttpResponse
from .bot.loader import bot, dp


async def proceed_update(req: HttpRequest):
    upd = types.Update(**(json.loads(req.body)))
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(upd)


