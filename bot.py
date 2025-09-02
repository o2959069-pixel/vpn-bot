import os
from aiogram import Bot, Dispatcher, executor, types

# Токен берём из переменной окружения (Render -> Переменные окружения)
BOT_TOKEN = os.getenv("8444347725:AAEIjERypbS7uZEtLvTU3kteMGfDTVTEqzU")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.reply("Привет! 👋 Напиши /key, чтобы получить VPN ключ 🔑")

# Команда /key
@dp.message_handler(commands=['key'])
async def key(msg: types.Message):
    # Здесь можно вставить свой реальный ключ VPN или временный
    await msg.reply("vless://1234-5678-90ab-cdef@1.2.3.4:443")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
