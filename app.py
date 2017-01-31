from flask import Flask, render_template, request, redirect
from config import APP_SETTINGS
from forms import db

import json
app = Flask(__name__)
app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
PRODUCTS_PER_PAGE = 20
from forms import FinishedProductForm, BrandForm, Product, SupplierForm, Production, ProductionNeeds, ProductionNeedsForm, Brand, Purchase, Sale, Supplier, ToolForm, CompoundForm


forms = dict(product=(FinishedProductForm, Product, dict(type_="finished", unit="un"), 'add.html', 'brand', False),
             tool=(ToolForm, Product, dict(type_="tool", unit="un"), "add.html", 'brand', True),
             compound=(CompoundForm, Product, dict(type_="compound"), 'add.html', 'brand', True),
             brand=(BrandForm, Brand, dict(), 'add.html', 'supplier', True),
             supplier=(SupplierForm, Supplier, dict(), 'add.html', '', True))

types = dict(product="finished", tool="tool", compound="compound")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add/<item>', methods=['GET', 'POST'])
def add(item):
    form_class, item_class, kwargs, template, choices, redirect_form = forms[item]
    form = form_class(request.form)
    if choices == 'brand':
        form.brand.choices = [(b.id_, b.name) for b in Brand.query.all()]
    elif choices == "supplier":
        form.supplier.choices = [(b.id_, b.name) for b in Supplier.query.all()]

    if request.method == 'POST' and form.validate():
        item_ = item_class(**form.data, **kwargs)
        db.session.add(item_)
        db.session.commit()
        if redirect_form:
            return redirect('/add/' + item)
        else:
            return redirect('see_product/' + item_.id_)
    return render_template(template, form=form, item=item)


@app.route('/add/component/<int:product_id>', methods=['POST'])
def add_component(product_id):
    form = ProductionNeedsForm(request.form)

    if request.method == 'POST':
        relation = ProductionNeeds(product_out=product_id, **form.data)
        db.session.add(relation)
        db.session.commit()
        return json.dumps({'success':True}), 201, {'ContentType':'application/json'}
    return json.dumps({'success':False}), 400, {'ContentType':'application/json'}


@app.route("/query_all/<string:type_>", methods=["GET"])
def query_all(type_):
    return Product.query.filter(Product.type_ == type_)


@app.route('/see_products', methods=['GET', 'POST'])
@app.route('/see_products/<int:page>', methods=['GET', 'POST'])
def see_products(page=1):
    products = Product.query.paginate(page, PRODUCTS_PER_PAGE, False)
    return render_template('see_products.html', products=products)


@app.route('/see_product/<int:product_id>', methods=['GET'])
def see_product(product_id):
    product = Product.query.get(product_id)
    return render_template('see_product.html', product=product)


@app.route('/product/get_unit/<int:product_id>')
def get_unit_for_product(product_id):
    product = Product.query.get(product_id)
    return product.unit


@app.route('/product/get_all_choices')
def get_all_products():
    return "".join(['<option value="{}">{}</option>'.format(p.id_, p.name) for p in Product.query.all()])


if __name__ == '__main__':
    app.run()
