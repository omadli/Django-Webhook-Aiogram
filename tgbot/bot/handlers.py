from aiogram import types
from .loader import bot, dp


@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(f"Salom {message.from_user.get_mention(as_html=True)}")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)

