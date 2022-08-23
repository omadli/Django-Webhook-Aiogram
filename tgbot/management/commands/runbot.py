from django.core.management.base import BaseCommand, CommandError
from tgbot.bot.loader import bot, dp
from tgbot.bot.handlers import *
from aiogram import executor


class Command(BaseCommand):
    help = 'Run bot in poolling'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Bot started"))
        executor.start_polling(dp, skip_updates=True)
    