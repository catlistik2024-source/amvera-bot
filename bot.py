import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

API_TOKEN = "YOUR_BOT_TOKEN"
API_URL = "https://your-amvera-domain.amvera.io"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я - бот Ресторана спонтанной кухни.\n"
                        "Команды:\n"
                        "/menu - показать меню\n"
                        "/order <id> - сделать заказ блюда по ID\n"
                        "/announcement - показать объявление")

@dp.message_handler(commands=['menu'])
async def menu(message: types.Message):
    response = requests.get(f"{API_URL}/menu")
    if response.status_code == 200:
        menu = response.json()
        text = "Меню:\n"
        for dish in menu:
            text += f"{dish['id']}. {dish['name']} - {dish['price']}₽\n    {dish['description']}\n"
        await message.answer(text)
    else:
        await message.answer("Не удалось получить меню")

@dp.message_handler(commands=['announcement'])
async def announcement(message: types.Message):
    response = requests.get(f"{API_URL}/announcement")
    if response.status_code == 200:
        ann = response.json()
        await message.answer(f"Объявление: {ann['message']}")
    else:
        await message.answer("Не удалось получить объявление")

@dp.message_handler(commands=['order'])
async def order(message: types.Message):
    try:
        dish_id = int(message.text.split()[1])
    except (IndexError, ValueError):
        await message.answer("Пожалуйста, укажите ID блюда. Пример: /order 1")
        return
    order_data = {
        "user_id": message.from_user.id,
        "dish_ids": [dish_id]
    }
    response = requests.post(f"{API_URL}/order", json=order_data)
    if response.status_code == 200:
        await message.answer("Заказ принят! Спасибо.")
    else:
        await message.answer("Не удалось принять заказ. Попробуйте позже.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
