from app import db
from sqlalchemy import ForeignKey, PrimaryKeyConstraint


class Brand(db.Model):
    __tablename__ = 'brand'
    name = db.Column(db.String(100), primary_key=True)
    id = db.Column(db.Integer, autoincrement=True)
    abreviation = db.Column(db.String(10))


class Product(db.Model):
    __tablename__ = 'product'
    production_time = db.Column(db.Integer)
    name = db.Column(db.String(100))
    brand = db.Column(db.String(100), ForeignKey('brand.name'))
    unit = db.Column(db.String(10))
    type = db.Column(db.String(30))
    description = db.Column(db.String(255))
    code = db.Column(db.String(30), primary_key=True)
    id = db.Column(db.Integer, autoincrement=True)
    current_selling_price = db.Column(db.Integer)
    current_quantity = db.Column(db.Integer)
    image = db.Column(db.Text)


class Purchase(db.Model):
    __tablename__ = 'purchase'
    product = db.Column(db.String(30), ForeignKey('product.code'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    entity = db.Column(db.String(255))
    action_date = db.Column(db.Integer)
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)


class Sale(db.Model):
    __tablename__ = 'sale'
    product = db.Column(db.String(30), ForeignKey('product.code'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    entity = db.Column(db.String(255))
    action_date = db.Column(db.Integer)
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)


class Produce(db.Model):
    __tablename__ = 'produce'
    product = db.Column(db.String(30), ForeignKey('product.code'))
    quantity = db.Column(db.Integer)
    action_date = db.Column(db.Integer)
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)


class Production_needs(db.Model):
    __tablename__ = 'production_needs'

    __table_args__ = (
        PrimaryKeyConstraint('product_out', 'product_in'),
    )

    product_out = db.Column(db.String(30), ForeignKey('product.code'))
    product_in = db.Column(db.String(30), ForeignKey('product.code'))
    quantity = db.Column(db.Integer)
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)












