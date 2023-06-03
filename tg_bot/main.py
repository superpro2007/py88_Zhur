import re

import telebot

import config

REGEX = r"(((\w+\s*)+)\n)((\d+)\n)((\d+)\n)(\d+)"

bot = telebot.TeleBot(config.TG_BOT_TOKEN, parse_mode='HTML')


def is_text_matches(message: telebot.types.Message) -> bool:
    result = re.match(REGEX, message.text, re.MULTILINE)
    if result is None:
        return False
    else:
        return True


def parse_food(text: str) -> dict:
    text_parts = re.findall(REGEX, text, re.MULTILINE)[0]
    name_product = text_parts[1]
    proteins = text_parts[4]
    fats = text_parts[6]
    carbohydrates = text_parts[7]
    return {
        'name': name_product,
        'proteins': proteins,
        'fats': fats,
        'carbohydrates': carbohydrates
    }


@bot.message_handler(func=is_text_matches)
def handle_food(message: telebot.types.Message):
    food = parse_food(message.text)
    food['user_id'] = message.from_user.id
    bot.reply_to(message=message, text='eda sohranena')
    print(food)


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
