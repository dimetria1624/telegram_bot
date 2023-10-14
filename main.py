import telebot
from telebot import types


bot = telebot.TeleBot(token='6531239639:AAHZo4spb5xhRhNtsW4gaAVpfzldMD6yyFQ')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id

    welcome_message = 'Добро пожаловать! Я ваш Telegram бот. Вы можете использовать следующие команды:'
    available_commands = '/start - Начать\n/help - Помощь'
    name = message.from_user.first_name
    bot.send_message(user_id,name + ' ' + welcome_message + available_commands)

@bot.message_handler(commands=['help'])
def help(message):
    user_id = message.chat.id
    help_text = 'Выберите действие:'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button1 = types.KeyboardButton('Узнать новости')
    button2 = types.KeyboardButton('Узнать погоду')
    button3 = types.KeyboardButton('Узнать мероприятия')
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(user_id, help_text, reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def text_message_handler(message):
    user_id = message.chat.id
    text = message.text
    if str(text).lower() == 'привет':
        bot.send_message(user_id, 'я занят !')
    else:
        bot.send_message(user_id, 'Здорова сначала !')

bot.polling(none_stop=True)