# Timing Attack Lab

Намеренно уязвимый Flask-сайт для изучения timing attacks.

## Локальный запуск

```bash
python -m pip install -r requirements.txt
python app.py
```

Откройте http://127.0.0.1:5000

## Развёртывание на Render

1. Создайте GitHub-репозиторий и загрузите эти файлы.
2. В Render выберите **New → Web Service** и подключите репозиторий.
3. Build Command:
   `pip install -r requirements.txt`
4. Start Command:
   `gunicorn app:app`
5. Создайте переменную окружения:
   `LAB_SECRET`
6. Укажите учебный секрет, который хотите использовать.
7. Выберите Free plan и создайте сервис.

Render выдаст публичный адрес вида:
`https://имя-сервиса.onrender.com`

Важно: это специально уязвимый демонстрационный сервер. Не используйте его
для настоящих аккаунтов, настоящих паролей или реальных пользовательских данных.
