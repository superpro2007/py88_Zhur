import telebot
import config

bot = telebot.TeleBot(config.TG_BOT_TOKEN, parse_mode='HTML')


@bot.message_handler(func=lambda m: True)
def invite(message):
    text = '''
vvedite edy v formate:

imya edi
koli4estvo belkov
koli4estvo zhirov
koli4estvo uglevodov


primer:

yabloko
1
1
10
'''
    bot.send_message(chat_id=message.from_user.id, text= text)


bot.infinity_polling()
