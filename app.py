from flask import Flask, render_template, request
from config import APP_SETTINGS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Product, Produce, Production_needs, Brand, Purchase, Sale
from forms import ProductForm, BrandForm


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm(request.form)
    if request.method == 'POST' and form.validate():
        product = Product(form.production_time.data, form.name.data,
                    form.brand.data, form.unit.data, form.type.data,
                    form.description.data, form.code.data, form.current_selling_price.data,
                    form.current_quantity.data, form.image.data)


        db.session.add(product)
        db.session.commit()
    return render_template('add_product.html', form=form)

@app.route('/add_brand', methods=['GET', 'POST'])
def add_brand():
    form = BrandForm(request.form)
    if request.method == 'POST' and form.validate():
        brand = Brand(form.name.data, form.abbreviation.data)
        db.session.add(brand)
        db.session.commit()
    return render_template('add_brand.html', form=form)


if __name__ == '__main__':
    app.run()
