from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="ТОКЕН_ОТ_BOTFATHER")  # вставь сюда свой токен от BotFather
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.reply("Привет! Напиши /key чтобы получить ключ.")

@dp.message_handler(commands=['key'])
async def key(msg: types.Message):
    await msg.reply("vless://1234-5678-90ab-cdef@1.2.3.4:443")

executor.start_polling(dp, skip_updates=True)
