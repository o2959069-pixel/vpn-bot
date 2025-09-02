from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

TOKEN = os.getenv("8444347725:AAEIjERypbS7uZEtLvTU3kteMGfDTVTEqzU")  # токен будет храниться в Render

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("📡 Подключиться"))
menu.add(KeyboardButton("🔑 Установить VPN"))
menu.add(KeyboardButton("🎁 Пригласить друзей"))
menu.add(KeyboardButton("🆘 Помощь"))
menu.add(KeyboardButton("📄 Оферта"))
menu.add(KeyboardButton("💵 Заработать с нами"))

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("Привет! Добро пожаловать в BoomVPN 👋", reply_markup=menu)

@dp.message_handler(lambda msg: msg.text == "📡 Подключиться")
async def connect(msg: types.Message):
    await msg.answer("Твой ключ: vless://1234-5678-90ab-cdef@1.2.3.4:443")

@dp.message_handler(lambda msg: msg.text == "🔑 Установить VPN")
async def install(msg: types.Message):
    await msg.answer("Скачай приложение VPN и вставь ключ, который я тебе дам.")

@dp.message_handler(lambda msg: msg.text == "🎁 Пригласить друзей")
async def friends(msg: types.Message):
    await msg.answer("Поделись ссылкой на бота и получи +10 дней доступа 😉")

@dp.message_handler(lambda msg: msg.text == "🆘
