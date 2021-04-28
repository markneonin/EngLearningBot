from loader import dp, bot
from data import *
from aiogram import types
from utils import create_text, services
from database import db_working as db
from aiogram.dispatcher import  FSMContext
from random import choice
from keyboards import *


@dp.message_handler(commands=['words'])
async def words(msg: types.Message, state: FSMContext):
	await state.finish()
	to_state = {}
	words = db.get_words([0,1])
	while len(to_state) < 5:
		word = choice(words)
		to_state[word] = True
	
	await state.update_data({msg.message_id : to_state})
	text = create_text.words(to_state)
	
	
	
	
	
	keyb = words_inline(to_state, msg.message_id)
	await bot.send_message(msg.from_user.id, text, reply_markup=keyb)