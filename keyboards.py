from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callbacks import *

def words_inline(words):
	buttons = []
	for i, (word, _) in enumerate(words.items()):
		buttons.append(InlineKeyboardButton(
        text=f'{i+1}',
        callback_data=show_translate_callback.new(word_id=word.word_id)))
	
	words_kb = InlineKeyboardMarkup(inline_keyboard=[[buttons[0],buttons[1]], [buttons[2], buttons[3]], [buttons[4]]])
	
	return words_kb