import re

import telebot

import config

REGEX = r"(\w+\s*)+\n\d+\n\d+\n\d+"

bot = telebot.TeleBot(config.TG_BOT_TOKEN, parse_mode='HTML')


def is_text_matches(message: telebot.types.Message) -> bool:
    result = re.match(REGEX, message.text, re.MULTILINE)
    if result is None:
        return False
    else:
        return True


@bot.message_handler(func=is_text_matches)
def handle_food(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message=message, text='eda sohranena')


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
