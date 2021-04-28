from loader import dp, bot
from data import *
from aiogram import types
from utils import create_text, services
from database import db_working as db

	
@dp.message_handler()
async def message (msg: types.Message):
	word = services.create_word_obj(msg.text)
	db.add_word(word)
	await bot.send_message(msg.from_user.id, f'Добавил!')