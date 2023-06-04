from flask import Flask

app = Flask(__name__)

@app.get('/food')
def food_get():
    return 'Hello world'

@app.post('/food')
def food_post():
    return 'Hello hui'