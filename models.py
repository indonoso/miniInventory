from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


db = SQLAlchemy()
association_table = db.Table('association', db.Column('brand', db.Integer, ForeignKey('brand.id_')),
                             db.Column('supplier', db.Integer, ForeignKey('supplier.id_')))


class Supplier(db.Model):
    __tablename__ = 'supplier'
    name = db.Column(db.String(100))
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    abbreviation = db.Column(db.String(10))
    address = db.Column(db.Text)
    comments = db.Column(db.Text)
    image = db.Column(db.Text)

    def __init__(self, name=None, abbreviation=None, address=None, comments=None, id_=None, **kwargs):
        self.name = name
        self.abbreviation = abbreviation
        self.address = address
        self.comments = comments
        self.id_ = id_
        self.image = image


class Brand(db.Model):
    __tablename__ = 'brand'
    name = db.Column(db.String(100))
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    abbreviation = db.Column(db.String(10))
    comments = db.Column(db.Text)
    image = db.Column(db.Text)
    suppliers = relationship("Supplier", secondary=association_table)

    def __init__(self, name=None, abbreviation=None, comments=None, id_=None, supplier=[], **kwargs):
        self.name = name
        self.abbreviation = abbreviation
        self.comments = comments
        self.id_ = id_
        self.suppliers = []
        self.image = image
        for s in supplier:
            self.suppliers.append(Supplier.query.get(s))




class Product(db.Model):
    __tablename__ = 'product'
    production_time = db.Column(db.Integer)
    name = db.Column(db.String(100))
    brand = db.Column(db.Integer, ForeignKey('brand.id_'))
    unit = db.Column(db.String(10))
    type_ = db.Column(db.String(30))
    description = db.Column(db.String(255))
    id_ = db.Column(db.Integer, primary_key=True, autoincrement=True)
    current_selling_price = db.Column(db.Integer)
    current_quantity = db.Column(db.Integer)
    image = db.Column(db.Text)
    color = db.Column(db.String(20))
    shape = db.Column(db.String(20))

    def __init__(self, production_time=None, name=None, brand=None, unit=None, description=None,
                 current_selling_price=None, current_quantity=None, image=None, id_=None, type_=None, color=None, shape=None,  **kwargs):
        self.production_time = production_time
        self.name = name
        self.brand = brand
        self.unit = unit
        self.type_ = type_
        self.description = description
        self.current_selling_price = current_selling_price
        self.current_quantity = current_quantity
        self.image = image
        self.id_ = id_
        self.shape = shape
        self.color = color


class ProductionNeeds(db.Model):
    __tablename__ = 'production_needs'
    product = db.Column(db.Integer, ForeignKey('product.id_'), nullable=False)
    product_in = db.Column(db.Integer, ForeignKey('product.id_'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    id_ = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)

    def __init__(self, product=None, product_in=None, quantity=None, id_=None, comment=None,  **kwargs):
        self.product = product
        self.product_in = product_in
        self.quantity = quantity
        self.id_ = id_
        self.comment = comment


class Purchase(db.Model):
    __tablename__ = 'purchase'
    product = db.Column(db.Integer, ForeignKey('product.id_'))
    supplier = db.Column(db.Integer, ForeignKey('supplier.id_'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    entity = db.Column(db.String(255))
    action_date = db.Column(db.Integer)
    id_ = db.Column(db.Integer, autoincrement=True, primary_key=True)

    def __init__(self, product=None, quantity=None, price=None, entity=None, action_date=None, id_=None,  **kwargs):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.entity = entity
        self.action_date = action_date
        self.id_ = id_


class Sale(db.Model):
    __tablename__ = 'sale'
    product = db.Column(db.Integer, ForeignKey('product.id_'))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    entity = db.Column(db.String(255))
    action_date = db.Column(db.Integer)
    id_ = db.Column(db.Integer, autoincrement=True, primary_key=True)

    def __init__(self, product=None, quantity=None, price=None, entity=None, action_date=None, id_=None,  **kwargs):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.entity = entity
        self.action_date = action_date
        self.id_ = id_


class Production(db.Model):
    __tablename__ = 'production'
    product = db.Column(db.Integer, ForeignKey('product.id_'))
    quantity = db.Column(db.Integer)
    action_date = db.Column(db.Integer)
    id_ = db.Column(db.Integer, autoincrement=True, primary_key=True)

    def __init__(self, product=None, quantity=None, action_date=None, id_=None,  **kwargs):
        self.product = product
        self.quantity = quantity
        self.action_date = action_date
        self.id_ = id_
