from flask import Flask
from config import APP_SETTINGS
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Product






@app.route('/')
def hello_world():
    return 'Hello World!'


def


if __name__ == '__main__':
    app.run()
