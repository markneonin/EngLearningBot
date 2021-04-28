from callbacks import show_translate_callback
from aiogram.types import CallbackQuery
from loader import bot, dp
from utils import create_text, services
from database import db_working as db
from aiogram.dispatcher import  FSMContext
from keyboards import *


@dp.callback_query_handler(show_translate_callback.filter())
async def showts_query(call: CallbackQuery, state: FSMContext):
	await call.answer(cache_time=1)
	
	message_id = call['message']['message_id']
	chat_id = call['message']['chat']['id']
	id = int(call.data.split(':')[1])
	data = await state.get_data()
	
	for word, hide in data.items():
		if word.word_id == id:
			if hide: data[word] = False
			else: data[word] = True
	
	await state.reset_data()
	await state.update_data(data)
	text = create_text.words(data)
	keyb = words_inline(data)
	
	await bot.edit_message_text(message_id=message_id, chat_id=chat_id, text=text)
	await bot.edit_message_reply_markup(message_id=message_id, chat_id=chat_id,
                                            reply_markup=keyb)
	