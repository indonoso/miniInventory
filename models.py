from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint

db = SQLAlchemy()


class Brand(db.Model):
    __tablename__ = 'brand'
    name = db.Column(db.String(100), primary_key=True)
    id_ = db.Column(db.Integer, autoincrement=True)
    abbreviation = db.Column(db.String(10))

    def __init__(self, name, abbreviation):
        self.name = name
        self.abbreviation = abbreviation


class Product(db.Model):
    __tablename__ = 'product'
    production_time = db.Column(db.Integer)
    name = db.Column(db.String(100))
    brand = db.Column(db.String(100), ForeignKey('brand.name'))
    unit = db.Column(db.String(10))
    type_ = db.Column(db.String(30))
    description = db.Column(db.String(255))
    code = db.Column(db.String(30), primary_key=True)
    id_ = db.Column(db.Integer, autoincrement=True)
    current_selling_price = db.Column(db.Integer)
    current_quantity = db.Column(db.Integer)
    image = db.Column(db.Text)

    def __init__(self, production_time, name, brand, unit, type_, description, code, current_selling_price,
                 current_quantity, image):
        self.production_time = production_time
        self.name = name
        self.brand = brand
        self.unit = unit
        self.type_ = type_
        self.description = description
        self.code = code
        self.current_selling_price = current_selling_price
        self.current_quantity = current_quantity
        self.image = image


class Production_needs(db.Model):
    __tablename__ = 'production_needs'
    product_out = db.Column(db.String(30), ForeignKey('product.code'))
    product_in = db.Column(db.String(30), ForeignKey('product.code'))
    quantity = db.Column(db.Integer)
    id_ = db.Column(db.Integer, autoincrement=True)

    __table_args__ = (
        PrimaryKeyConstraint('product_out', 'product_in'),
    )


def __init__(self, product_out, product_in, quantity, id_):
    self.product_out = product_out
    self.product_in = product_in
    self.quantity = quantity
    self.id_ = id_


class Purchase(db.Model):
    __tablename__ = 'purchase'
    product = db.Column(db.String(30), ForeignKey('product.code'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    entity = db.Column(db.String(255))
    action_date = db.Column(db.Integer)
    id_ = db.Column(db.Integer, autoincrement=True, primary_key=True)

    def __init__(self, product, quantity, price, entity, action_date, id_):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.entity = entity
        self.action_date = action_date
        self.id_ = id_


class Sale(db.Model):
    __tablename__ = 'sale'
    product = db.Column(db.String(30), ForeignKey('product.code'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    entity = db.Column(db.String(255))
    action_date = db.Column(db.Integer)
    id_ = db.Column(db.Integer, autoincrement=True, primary_key=True)

    def __init__(self, product, quantity, price, entity, action_date, id_):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.entity = entity
        self.action_date = action_date
        self.id_ = id_


class Produce(db.Model):
    __tablename__ = 'produce'
    product = db.Column(db.String(30), ForeignKey('product.code'))
    quantity = db.Column(db.Integer)
    action_date = db.Column(db.Integer)
    id_ = db.Column(db.Integer, autoincrement=True, primary_key=True)

    def __init__(self, product, quantity, action_date, id_):
        self.product = product
        self.quantity = quantity
        self.action_date = action_date
        self.id_ = id_
