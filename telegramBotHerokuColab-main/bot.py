import telebot
TOKEN = 'Вставь сюда токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.png', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🧡 Мой репозиторий")
	item2 = types.KeyboardButton("😋 Напиши мне в личку")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Привет тебе от Стича, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🧡 Мой репозиторий':
			bot.send_message(message.chat.id, 'https://github.com/IuliiaMikhailova')
		elif message.text == '😋 Напиши мне в личку':
			bot.send_message(message.chat.id, 'http://t.me/jullia_cherr')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)








#https://core.telegram.org/bots/api#available-methods
