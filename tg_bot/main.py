import telebot
import config

bot = telebot.TeleBot(config.TG_BOT_TOKEN, parse_mode='HTML')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text='darova chel')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
