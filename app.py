from flask import Flask, render_template, request
from config import APP_SETTINGS
from forms import db

app = Flask(__name__)
app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from forms import ProductForm, BrandForm, Product, Production, ProductionNeeds, Brand, Purchase, Sale, Supplier


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm(request.form)
    if request.method == 'POST' and form.validate():
        product = Product(**form.data)
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
