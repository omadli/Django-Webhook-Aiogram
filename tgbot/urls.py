from django.urls import path
from .views import home, telegram
from src.settings import WEBHOOK_PATH

urlpatterns = [
    path('', home, name='home'),
    path(WEBHOOK_PATH, telegram, name='webhook'),
]
