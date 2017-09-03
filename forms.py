from wtforms import BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField, SelectField, SelectMultipleField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import *


class SupplierForm(FlaskForm):
    name = StringField('Nombre del proveedor', [InputRequired(), Length(min=1, max=100)])
    abbreviation = StringField('Nombre abreviado', [InputRequired(), Length(min=1, max=10)])
    comments = TextAreaField("Comentarios sobre el proveedor")
    address = TextAreaField("Dirección del proveedor")
    image = FileField("Imagen", validators=[
        FileAllowed(['jpg', 'png', 'pdf'], 'Sólo imágenes o pdf')])  # StringField('Link público a la imagen', [InputRequired(), Length(min=1)])


class BrandForm(FlaskForm):
    name = StringField('Nombre de la marca', [InputRequired(), Length(min=1, max=100)])
    abbreviation = StringField('Nombre abreviado', [InputRequired(), Length(min=1, max=10)])
    comments = TextAreaField("Comentarios sobre la marca")
    supplier = SelectMultipleField("Proveedores", coerce=int, choices=[], default=1)
    image = FileField("Imagen", validators=[
        FileAllowed(['jpg', 'png', 'pdf'], 'Sólo imágenes o pdf')])  # StringField('Link público a la imagen', [InputRequired(), Length(min=1)])


class FinishedProductForm(FlaskForm):
    name = StringField('Nombre', [InputRequired()])
    brand = StringField('Marca', render_kw={'autocomplete': "off"})
    production_time = IntegerField('Tiempo mínimo de producción', [InputRequired()], render_kw={"placeholder": "En horas"})
    description = TextAreaField('Descripción')
    current_selling_price = IntegerField('Precio de venta')
    current_quantity = IntegerField('Cantidad actual en inventario')
    image = FileField("Imagen", validators=[FileAllowed(['jpg', 'png', 'pdf'], 'Sólo imágenes o pdf')]) #StringField('Link público a la imagen', [InputRequired(), Length(min=1)])
    color = StringField("Color", [InputRequired(), Length(min=1)])
    shape = StringField("Forma", [InputRequired(), Length(min=1)])


class CompoundForm(FlaskForm):
    name = StringField('Nombre', [validators.required()])
    unit = SelectField('Unidad de medida', coerce=str,
                       choices=[('kg', 'Kilos'), ('mt', "Metros"), ('lt', "Litros"), ("un", "Unidad")], default=3, render_kw={'autocomplete': "off"})
    brand = StringField('Marca', render_kw={'autocomplete': "off"})
    description = TextAreaField('Descripción')
    current_selling_price = IntegerField('Precio de venta')
    current_quantity = IntegerField('Cantidad actual en inventario')
    color = StringField("Color", [InputRequired(), Length(min=1)], render_kw={"placeholder": "Solo si corresponde"})
    shape = StringField("Forma", [InputRequired(), Length(min=1)], render_kw={"placeholder": "Solo si corresponde"})
    image = FileField("Imagen", validators=[
        FileAllowed(['jpg', 'png', 'pdf'], 'Sólo imágenes o pdf')])  # StringField('Link público a la imagen', [InputRequired(), Length(min=1)])


class ToolForm(FlaskForm):
    name = StringField('Nombre', [validators.required()])
    brand = StringField('Marca', render_kw={'autocomplete': "off"})
    description = TextAreaField('Descripción')
    current_selling_price = IntegerField('Precio de venta')
    current_quantity = IntegerField('Cantidad actual en inventario')
    image = StringField('Link público a la imagen', [Length(min=1)])
    color = StringField("Color", [InputRequired(), Length(min=1)], render_kw={"placeholder": "Solo si corresponde"})
    shape = StringField("Forma", [InputRequired(), Length(min=1)], render_kw={"placeholder": "Solo si corresponde"})


class ProductionNeedsForm(FlaskForm):
    product_in = SelectField('Insumo/Herramienta', [InputRequired], coerce=int, choices=[])
    quantity = IntegerField('Cantidad', [InputRequired()])
    comment = TextAreaField('Objetivo', render_kw={"placeholder": "Sirve para?"})


class PurchaseForm(FlaskForm):
    product = StringField('product')
    quantity = IntegerField('quantity')
    price = IntegerField('price')
    entity = StringField('entity')
    action_date = IntegerField('action_date')


class SaleForm(FlaskForm):
    product = StringField('product')
    quantity = IntegerField('quantity')
    price = IntegerField('price')
    entity = StringField('entity')
    action_date = IntegerField('action_date')


class ProduceForm(FlaskForm):
    product = StringField('product')
    quantity = IntegerField('quantity')
    action_date = IntegerField('action_date')

