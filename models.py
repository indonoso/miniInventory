from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import ForeignKey


class Product(db.Model):
    __product__ = 'results'

    name = db.Column(db.String(100))
    production_time = db.Column(db.Integer)
    brand = db.Column(db.String(100), ForeignKey("brand.name"))

    def __init__(self, url, result_all, result_no_stop_words):
        self.url = url
        self.result_all = result_all
        self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<id {}>'.format(self.id)


"""
  production_time int,
  name VARCHAR(100),
  brand VARCHAR(100) REFERENCES brand(name),
  unit VARCHAR(10),
  type VARCHAR(30),
  description VARCHAR(255),
  codigo VARCHAR(30) PRIMARY KEY,
  id SERIAL,
  current_selling_price int,
  current_quantity int,
  image text
"""
