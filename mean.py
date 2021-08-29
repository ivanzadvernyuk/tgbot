#  1904040366:AAE5IhjNqxJkqBnA5z0XNlhoNSlf7Kk58-0
import telebot
from telebot import types
name = ''
username=''
age = 0

bot = telebot.TeleBot("1904040366:AAE5IhjNqxJkqBnA5z0XNlhoNSlf7Kk58-0")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Добро пожаловать!")
@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "В настоящее время отсутствуют функции бота.")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == 'Привет':
		bot.reply_to(message, 'Привет, тестовый пользователь!')
	elif message.text == '/reg':
		bot.send_message(message.from_user.id, "Давай познакомимся! Как тебя зовут?")
		bot.register_next_step_handler(message, reg_name)

def reg_name(message):
	global name
	name = message.text
	bot.send_message(message.from_user.id, "Создайте имя пользователя")
	bot.register_next_step_handler(message, reg_username)

def reg_username(message):
	global username
	username = message.text
	bot.send_message(message.from_user.id, "Для завершения регистрации введите Ваш возраст")
	bot.register_next_step_handler(message, reg_age)

def reg_age(message):
	global age
	age = message.text
	while age == 0:
		try:
			age = int(message.text)
		except Exception:
			bot.send_message(message.from_user.id, "Вводите цифрами")

	keyboard = types.InlineKeyboardMarkup()
	key_yes = types.InlineKeyboardButton(text='Да', callback_data= 'yes')
	keyboard.add(key_yes)
	key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
	keyboard.add(key_no)
	question = "Тебе " + str(age) + ' лет? И тебя зовут '+ name + '?'
	bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if call.data == "yes":
		bot.send_message(call.message.chat.id, 'Супер! Приятно познакомиться!')
	elif call.data == "no":
		bot.send_message(call.message.chat.id, 'Извините, попробуем ещё раз')
		bot.send_message(call.message.chat.id, "Давай познакомимся! Как тебя зовут?")
		bot.register_next_step_handler(call.message, reg_name)



bot.polling()