from django.core.management.base import BaseCommand, CommandError
from tgbot.bot.loader import bot
from asgiref.sync import async_to_sync


class Command(BaseCommand):
    help = 'Deleting webhook'

    def handle(self, *args, **options):
        webhook = async_to_sync(bot.get_webhook_info)()
        if webhook.url != "":
            async_to_sync(bot.delete_webhook)()
            self.stdout.write(self.style.SUCCESS('Webhook was successfully deleted!'))
        else:
            self.stdout.write(self.style.WARNING('Webhook no setted!'))
    