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


forms = dict(finished=(FinishedProductForm, Product, dict(type_="finished", unit="un"), 'add.html', 'brand', False),
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
        form.supplier.choices = [(s.id_, s.name) for s in Supplier.query.all()]

    if request.method == 'POST' and form.validate():
        form.data['brand'] = int(form.data['brand'])
        item_ = item_class(**form.data, **kwargs)
        db.session.add(item_)
        db.session.commit()
        if redirect_form:
            return redirect('/add/' + item)
        else:
            return redirect('see_item/{}/{}'.format(item, str(item_.id_)))
    return render_template(template, form=form, item=item, items=json.dumps([{'id': b.id_, 'title': b.name} for b in Brand.query.all()]))


@app.route('/add/component/<int:product_id>', methods=['POST', 'PUT'])
def add_component(product_id):
    form = ProductionNeedsForm(request.form)
    if form.data["product_in"]:
        if request.method == 'POST':
            relation = ProductionNeeds(product=product_id, **form.data)
            db.session.add(relation)
            db.session.commit()
            return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
        elif request.method == 'PUT':
            relation = ProductionNeeds.query.all().filter(product_out=product_id, product_in=form.data["product_in"]).first()
            for k, v in form.data:
                if relation.__dict__[k] != v:
                    relation.__dict__[k] = v
            db.session.commit()
            return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    return json.dumps({'success': False}), 400, {'ContentType': 'application/json'}


@app.route("/query_all/<string:type_>", methods=["GET"])
def query_all(type_):
    return Product.query.filter(Product.type_ == type_)


@app.route('/see_all/<item>', methods=['GET'])
@app.route('/see_all/<item>/<int:page>', methods=['GET'])
def see_all(item, page=1):
    if item in ["finished", "compound", "tool"]:
        all_items = Product.query.filter(Product.type_ == item).paginate(page, PRODUCTS_PER_PAGE, False)
    elif item == "supplier":
        all_items = Supplier.query.paginate(page, PRODUCTS_PER_PAGE, False)
    elif item == "brand":
        all_items = Brand.query.paginate(page, PRODUCTS_PER_PAGE, False)
    return render_template('see_all.html', all_items=all_items, item_type=item)


@app.route('/see_item/<item>/<int:item_id>', methods=['GET'])
def see_item(item, item_id):
    products = None
    products_in = None
    products_in_names = None
    if item in ["finished", "compound", "tool"]:
        item = Product.query.get(item_id)
        products = Product.query.all()
        products_in = ProductionNeeds.query.filter(ProductionNeeds.product == item_id).all()
        products_in_names = dict()
        for p in products_in:
            products_in_names[p.product_in] = Product.query.filter(Product.id_ == p.product_in).first().name
    elif item == "supplier":
        item = Supplier.query.get(item_id)
    elif item == "brand":
        item = Brand.query.get(item_id)

    return render_template('see_item.html', item=item, products=products, products_in=products_in, products_in_names=products_in_names)


@app.route('/product/get_unit/<int:product_id>')
def get_unit_for_product(product_id):
    product = Product.query.get(product_id)
    return product.unit


if __name__ == '__main__':
    app.run()
