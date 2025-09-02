import os
from aiogram import Bot, Dispatcher, executor, types

# Если хочешь — можно вставить токен прямо сюда:
# BOT_TOKEN = "8444347725:AAEIjERypbS7uZEtLvTU3kteMGfDTVTEqzU"

# Но лучше хранить в переменных окружения (например, на Render, Heroku и т.д.)
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Команда /start
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.reply("Привет! Напиши /key чтобы получить ключ.")

# Команда /key
@dp.message_handler(commands=['key'])
async def key(msg: types.Message):
    # Здесь можно вставить свой реальный VPN-ключ (например VLESS или WireGuard)
    await msg.reply("vless://1234-5678-90ab-cdef@1.2.3.4:443")

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
