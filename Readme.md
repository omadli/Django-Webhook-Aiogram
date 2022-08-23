# Django Webhook Aiogram

`aiogram` kutubxonasida yasalgan telegram botni `django`da *webhook* qilish uchun shablon.
Oddiy `echobot` misolida!

## Dastlabki ishlar:

Birinchi bo'lib kerakli kutubxonalarni o'rnating:
```bash
$ pip install -r requirements.txt
```
Keyingi ish __Environment variables__ uchun `.env.example` faylidan nusxa olib yarating va shuning ichiga Bot tokeni, Web saytingiz domenini (https protokolda) Secret key va `DEBUG` parametrlarini kiriting:
```bash
$ cp .env.example .env
```

## Management commands

Boshqaruv buyruqlari:
- `runbot` telegram botni *long poolling*da ishga tushiradi. (Saytingiz bo'lmasa yoki serverga qo'ymagan bo'lsangiz botni ishlashini tekshirib ko'rish uchun) **Django ishlamaydi!**
- `setwebhook` botni birinchi marta dastlabki webhook qilib olish uchun
- `deletewebhook` webhookni uzish uchun
- `runserver` odatdagidek django serverni ishga tushiradi. Telegram bot webhhok ulangan bo'lsa ishlayveradi.


## Umumiy
Kerakli kutubxonalarni o'rnatgach va sozlash ishlarini (environment variables) bajargach:

1-ish:
```bash
$ python manage.py setwebhook
```
2-ish 
```bash
$ python manage.py runserver
``` 

## Eslatma

Bu faqat SSL sertifikatga ega web domenga ega serverlarda ishlaydi. Agar sizda domen bo'lmasa lokal kompyuteringizda sinab ko'rmoqchi bo'lsangiz `ngrok` ishlating. `WEB_DOMAIN` ga xuddi o'sha `ngrok` bergan domenni kiritsangiz bo'ldi.



&copy; Murodillo😎