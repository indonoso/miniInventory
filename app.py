from flask import Flask, render_template, request
from config import APP_SETTINGS
from forms import db

app = Flask(__name__)
app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
PRODUCTS_PER_PAGE = 20
from forms import FinishedProductForm, BrandForm, Product, SupplierForm ,Production, ProductionNeeds, Brand, Purchase, Sale, Supplier, ToolForm, CompoundForm


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = FinishedProductForm(request.form)
    form.brand.choices = [(b.id_, b.name) for b in Brand.query.all()]
    if request.method == 'POST' and form.validate():
        product = Product(**form.data, type_="finished", unit="un")
        db.session.add(product)
        db.session.commit()
    return render_template('add_product.html', form=form)


@app.route('/see_products', methods=['GET', 'POST'])
@app.route('/see_products/<int:page>', methods=['GET', 'POST'])
def see_products(page=1):
    products = Product.query.paginate(page, PRODUCTS_PER_PAGE, False).items
    return render_template('see_products.html', products=products)


@app.route('/see_product/<int:product_id>', methods=['GET'])
def see_product(product_id):
    product = Product.query.get(product_id)
    return render_template('see_product.html', product=product)


@app.route('/add_tool', methods=['GET', 'POST'])
def add_tool():
    form = ToolForm(request.form)
    form.brand.choices = [(b.id_, b.name) for b in Brand.query.all()]
    if request.method == 'POST' and form.validate():
        product = Product(**form.data, type_="tool", unit="un")
        db.session.add(product)
        db.session.commit()
    return render_template('add_tool.html', form=form)


@app.route('/add_compound', methods=['GET', 'POST'])
def add_compound():
    form = CompoundForm(request.form)
    form.brand.choices = [(b.id_, b.name) for b in Brand.query.all()]
    if request.method == 'POST' and form.validate():
        product = Product(**form.data, type_="compound")
        db.session.add(product)
        db.session.commit()
    return render_template('add_compound.html', form=form)


@app.route('/add_brand', methods=['GET', 'POST'])
def add_brand():
    form = BrandForm(request.form)
    if request.method == 'POST' and form.validate():
        brand = Brand(**form.data)
        db.session.add(brand)
        db.session.commit()
    return render_template('add_brand.html', form=form)


@app.route('/add_supplier', methods=['GET', 'POST'])
def add_supplier():
    form = SupplierForm(request.form)
    if request.method == 'POST' and form.validate():
        brand = Supplier(**form.data)
        db.session.add(brand)
        db.session.commit()
    return render_template('add_supplier.html', form=form)


if __name__ == '__main__':
    app.run()
