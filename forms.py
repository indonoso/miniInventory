from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField, SelectField
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField


class NewProductForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


class BrandForm(Form):
    name = StringField('Nombre de la marca', [validators.Length(min=1, max=100)])
    #id = IntegerField('id')
    abbreviation = StringField('Nombre abreviado', [validators.Length(min=1, max=10)])


class ProductForm(Form):
    production_time = IntegerField('Tiempo mínimo de producción')
    name = StringField('Nombre')
    brand = StringField('Marca')
    unit = StringField('Unidad de medida')
    type = SelectField('Tipo de producto', coerce=str, choices=[("finished", "Terminado"), ("intermediate", "Intermedio"), ("tool", "Herramienta"), ("insumos", "Insumo")])
    description = TextAreaField('Descripción')
    code = StringField('Código')
    #id = IntegerField('id')
    current_selling_price = IntegerField('Precio de venta')
    current_quantity = IntegerField('Cantidad actual en inventario')
    image = StringField('Link público a la imagen', [validators.Length(min=1)])

class Production_needsForm(Form):
    product_out = StringField('product_out')
    product_in = StringField('product_in')
    quantity = IntegerField('quantity')
    id = IntegerField('id')

class PurchaseForm(Form):
    product = StringField('product')
    quantity = IntegerField('quantity')
    price = IntegerField('price')
    entity = StringField('entity')
    action_date = IntegerField('action_date')
    id = IntegerField('id')

class SaleForm(Form):
    product = StringField('product')
    quantity = IntegerField('quantity')
    price = IntegerField('price')
    entity = StringField('entity')
    action_date = IntegerField('action_date')
    id = IntegerField('id')

class ProduceForm(Form):
    product = StringField('product')
    quantity = IntegerField('quantity')
    action_date = IntegerField('action_date')
    id = IntegerField('id')

