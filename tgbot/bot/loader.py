from src.settings import API_TOKEN
from aiogram import Bot, Dispatcher, types

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

