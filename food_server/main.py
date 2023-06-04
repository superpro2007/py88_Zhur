import re

import psycopg2

import config

REGEX = r"(((\w+\s*)+)\n)((\d+)\n)((\d+)\n)(\d+)"



def is_text_matches(message: telebot.types.Message) -> bool:
    result = re.match(REGEX, message.text, re.MULTILINE)
    if result is None:
        return False
    else:
        return True


def save_to_db(food: dict):
    conn = psycopg2.connect(f"dbname={config.DB_NAME} user={config.DB_USER} password={config.DB_PASSWORD} "
                            f"host={config.DB_HOST} port={config.DB_PORT}")
    cur = conn.cursor()
    cur.execute("INSERT INTO food (name, proteins, fats, carbohydrates, user_id) VALUES (%s, %s, %s, %s, %s)",
                (food['name'], food['proteins'], food['fats'], food['carbohydrates'], food['user_id']))
    conn.commit()
    cur.close()
    conn.close()

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


def handle_food(message: telebot.types.Message):
    food = parse_food(message.text)
    food['user_id'] = message.from_user.id
    save_to_db(food)
    print('eda sohranena')

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
    print(text)

