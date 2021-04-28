from loader import dp, bot
from data import start_message
from aiogram import types

@dp.message_handler(commands=['start'])
async def test(msg: types.Message):
	await bot.send_message(msg.from_user.id, start_message)