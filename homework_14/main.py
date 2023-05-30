import psycopg2


def ask_for_product() -> map:
    product_name = input('enter product name: \n')
    proteins = input('enter proteins amount: \n')
    fats = input('enter fats amount: \n')
    carbohydrates = input('enter carbohydrates amount: \n')
    product = {
        'name': product_name,
        'proteins': proteins,
        'fats': fats,
        'carbohydrates': carbohydrates
    }
    return product


def save_to_db(product: map):
    conn = psycopg2.connect("dbname=my_db user=my_user password=my_password host=localhost port=5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, proteins, fats, carbohydrates) VALUES (%s, %s, %s, %s)",
                (product['name'], product['proteins'], product['fats'], product['carbohydrates']))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    product = ask_for_product()
    save_to_db(product)
