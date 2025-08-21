# Ресторан спонтанной кухни - FastAPI + Telegram Bot

## Структура проекта
- main.py - FastAPI backend
- bot.py - Telegram бот (aiogram)
- requirements.txt - зависимости
- amvera.yml - конфигурация для Amvera Cloud
- .gitignore - стандартный
- README.md - инструкция

## Запуск локально
1. Установите Python 3.10+
2. Установите зависимости `pip install -r requirements.txt`
3. Запустите сервер командой `uvicorn main:app --reload`
4. Запустите телеграм-бота: `python bot.py`

## Выгрузка на Amvera Cloud и деплой

1. Зарегистрируйтесь и создайте проект на Amvera Cloud.
2. Инициализируйте git в папке проекта:
