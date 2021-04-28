from database.models import *

def create_word_obj(text):
	parts = text.split()
	en = ' '.join([parts[0], parts[1]])
	ru = parts[2]
	type = int(parts[3])
	word = Word(
	en=en, 
	ru=ru, 
	type=type)
	
	return word