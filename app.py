from flask import Flask
from flask import render_template
from tinydb import TinyDB
import random
db = TinyDB('db.json')
app = Flask(__name__)


@app.route('/')
def send_recipe():
    recipe = random_recipe(db)
    return render_template('recipes.html', name=recipe)


def random_recipe(database):
    return(random.choice(list(database)))
