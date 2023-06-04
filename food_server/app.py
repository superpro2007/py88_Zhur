from flask import Flask
from flask import request
import storage
app = Flask(__name__)

@app.get('/food')
def food_get():
    return 'Hello world'

@app.post('/food')
def food_post():
    for food in request.json:
        storage.save_to_db(food)
    return 'ok'
