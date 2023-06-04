
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

