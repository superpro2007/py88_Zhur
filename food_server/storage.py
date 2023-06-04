
import psycopg2

import config

def save_to_db(food: dict):
    conn = psycopg2.connect(f"dbname={config.DB_NAME} user={config.DB_USER} password={config.DB_PASSWORD} "
                            f"host={config.DB_HOST} port={config.DB_PORT}")
    cur = conn.cursor()
    cur.execute("INSERT INTO food (name, proteins, fats, carbohydrates, user_id) VALUES (%s, %s, %s, %s, %s)",
                (food['name'], food['proteins'], food['fats'], food['carbohydrates'], food['user_id']))
    conn.commit()
    cur.close()
    conn.close()

def get_food(user_id: int)->[dict]:
    conn = psycopg2.connect(f"dbname={config.DB_NAME} user={config.DB_USER} password={config.DB_PASSWORD} "
                            f"host={config.DB_HOST} port={config.DB_PORT}")
    cur = conn.cursor()
    cur.execute("SELECT * FROM food WHERE user_id = %s", (user_id,))
    food_list = cur.fetchall()
    response_food = []
    for food in food_list:
        response_food.append({
            'name': food[1],
            'proteins': food[2],
            'fats': food[3],
            'carbohydrates': food[4],
            'created_at': food[5],
            'user_id': food[6]
        })
    cur.close()
    conn.close()
    return response_food