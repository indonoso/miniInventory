from wtforms import BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField, SelectField
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import *





class SupplierForm(FlaskForm):
    name = StringField('Nombre del proveedor', [validators.required(), validators.Length(min=1, max=100)])
    abbreviation = StringField('Nombre abreviado', [validators.required(), validators.Length(min=1, max=10)])
    comments = TextAreaField("Comentarios sobre el proveedor")
    address = TextAreaField("Dirección del proveedor")



class BrandForm(FlaskForm):
    name = StringField('Nombre de la marca', [validators.required(), validators.Length(min=1, max=100)])
    abbreviation = StringField('Nombre abreviado', [validators.required(), validators.Length(min=1, max=10)])
    comments = TextAreaField("Comentarios sobre la marca")


class ProductForm(FlaskForm):

    name = StringField('Nombre', [validators.required()])
    unit = SelectField('Unidad de medida', coerce=str,
                       choices=[('kg', 'Kilos'), ('mt', "Metros"), ('lt', "Litros"), ("un", "Unidad")], default=3)
    brand = QuerySelectField('Proveedor', query_factory=lambda: Brand.query.all)
    production_time = IntegerField('Tiempo mínimo de producción', [validators.required()], render_kw={"placeholder": "En horas"})

    # type = SelectField('Tipo de producto', coerce=str, choices=[("finished", "Terminado"), ("intermediate", "Intermedio"), ("tool", "Herramienta"), ("insumos", "Insumo")])

    description = TextAreaField('Descripción')
    code = StringField('Código')
    #id = IntegerField('id')
    current_selling_price = IntegerField('Precio de venta')
    current_quantity = IntegerField('Cantidad actual en inventario')
    image = StringField('Link público a la imagen', [validators.Length(min=1)])


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

