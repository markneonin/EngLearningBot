from random import choice


def words(words):
	
	text = ''
	for i, (word, hide) in enumerate(words.items()):
		part = f'{i+1}){word.en} — '
		if hide: part += '🤔' + '\n'
		else: part += word.ru + ' ✔️\n'
		text += part
	text +=  '\n\nНажми на кнопку с номером слова, чтобы увидеть его перевод:'
	return text