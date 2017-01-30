from wtforms import BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField, SelectField, SelectMultipleField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import *


class SupplierForm(FlaskForm):
    name = StringField('Nombre del proveedor', [InputRequired(), Length(min=1, max=100)])
    abbreviation = StringField('Nombre abreviado', [InputRequired(), Length(min=1, max=10)])
    comments = TextAreaField("Comentarios sobre el proveedor")
    address = TextAreaField("Dirección del proveedor")


class BrandForm(FlaskForm):
    name = StringField('Nombre de la marca', [InputRequired(), Length(min=1, max=100)])
    abbreviation = StringField('Nombre abreviado', [InputRequired(), Length(min=1, max=10)])
    comments = TextAreaField("Comentarios sobre la marca")
    supplier = SelectMultipleField("Proveedores", coerce=int, choices=[], default=1)


class FinishedProductForm(FlaskForm):
    name = StringField('Nombre', [InputRequired()])
    brand = SelectField('Marca', coerce=int,  choices=[])
    production_time = IntegerField('Tiempo mínimo de producción', [InputRequired()], render_kw={"placeholder": "En horas"})
    description = TextAreaField('Descripción')
    current_selling_price = IntegerField('Precio de venta')
    current_quantity = IntegerField('Cantidad actual en inventario')
    image = StringField('Link público a la imagen', [InputRequired(), Length(min=1)])
    color = StringField("Color", [InputRequired(), Length(min=1)])
    shape = StringField("Forma", [InputRequired(), Length(min=1)])


class CompoundForm(FlaskForm):
    name = StringField('Nombre', [validators.required()])
    unit = SelectField('Unidad de medida', coerce=str,
                       choices=[('kg', 'Kilos'), ('mt', "Metros"), ('lt', "Litros"), ("un", "Unidad")], default=3)
    brand = SelectField('Marca', coerce=int,  choices=[])
    description = TextAreaField('Descripción')
    current_selling_price = IntegerField('Precio de venta')
    current_quantity = IntegerField('Cantidad actual en inventario')
    image = StringField('Link público a la imagen', [Length(min=1)])
    color = StringField("Color", [InputRequired(), Length(min=1)], render_kw={"placeholder": "Solo si corresponde"})
    shape = StringField("Forma", [InputRequired(), Length(min=1)], render_kw={"placeholder": "Solo si corresponde"})


class ToolForm(FlaskForm):
    name = StringField('Nombre', [validators.required()])
    brand = SelectField('Marca', coerce=int, choices=[])
    description = TextAreaField('Descripción')
    current_selling_price = IntegerField('Precio de venta')
    current_quantity = IntegerField('Cantidad actual en inventario')
    image = StringField('Link público a la imagen', [Length(min=1)])
    color = StringField("Color", [InputRequired(), Length(min=1)], render_kw={"placeholder": "Solo si corresponde"})
    shape = StringField("Forma", [InputRequired(), Length(min=1)], render_kw={"placeholder": "Solo si corresponde"})


class ProductionNeedsForm(FlaskForm):
    product_out = StringField('product_out')
    product_in = StringField('product_in')
    quantity = IntegerField('quantity')
    id = IntegerField('id')


class PurchaseForm(FlaskForm):
    product = StringField('product')
    quantity = IntegerField('quantity')
    price = IntegerField('price')
    entity = StringField('entity')
    action_date = IntegerField('action_date')
    id = IntegerField('id')


class SaleForm(FlaskForm):
    product = StringField('product')
    quantity = IntegerField('quantity')
    price = IntegerField('price')
    entity = StringField('entity')
    action_date = IntegerField('action_date')
    id = IntegerField('id')


class ProduceForm(FlaskForm):
    product = StringField('product')
    quantity = IntegerField('quantity')
    action_date = IntegerField('action_date')
    id = IntegerField('id')

