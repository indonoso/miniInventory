from flask import Flask
from config import APP_SETTINGS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Product, Produce, Production_needs, Brand, Purchase, Sale


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
