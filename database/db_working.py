from database.database import Session
from database.models import *


def add_word(word):
	session = Session()
	session.add(word)
	session.commit()
	session.close()


def get_words(types):
	session = Session()
	words = session.query(Word).filter(Word.type.in_(types)).all()
	session.close()
	return words
	