from flask import Flask, render_template, request, redirect
from config import APP_SETTINGS
from forms import db

app = Flask(__name__)
app.config.from_object(APP_SETTINGS)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
PRODUCTS_PER_PAGE = 20
from forms import FinishedProductForm, BrandForm, Product, SupplierForm, Production, ProductionNeeds, Brand, Purchase, Sale, Supplier, ToolForm, CompoundForm


forms = dict(product=(FinishedProductForm, Product, dict(type_="finished", unit="un"), 'add_product.html', 'brand'),
             tool=(ToolForm, Product, dict(type_="tool", unit="un"), "add_tool.html", 'brand'),
             compound=(CompoundForm, Product, dict(type_="compound") , 'add_compound.html', 'brand'),
             brand=(BrandForm, Brand, dict(), 'add_brand.html', 'supplier'),
             supplier=(SupplierForm, Supplier, dict(), 'add_supplier.html', ''))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add/<item>', methods=['GET', 'POST'])
def add(item):
    form_class, item_class, kwargs, template, choices = forms[item]
    form = form_class(request.form)
    if choices == 'brand':
        form.brand.choices = [(b.id_, b.name) for b in Brand.query.all()]
    elif choices == "supplier":
        form.supplier.choices = [(b.id_, b.name) for b in Supplier.query.all()]

    if request.method == 'POST' and form.validate():
        item_ = item_class(**form.data, **kwargs)
        db.session.add(item_)
        db.session.commit()
        return redirect('/add/' + item)
    return render_template(template, form=form, item=item)


@app.route('/see_products', methods=['GET', 'POST'])
@app.route('/see_products/<int:page>', methods=['GET', 'POST'])
def see_products(page=1):
    products = Product.query.paginate(page, PRODUCTS_PER_PAGE, False)
    return render_template('see_products.html', products=products)


@app.route('/see_product/<int:product_id>', methods=['GET'])
def see_product(product_id):
    product = Product.query.get(product_id)
    return render_template('see_product.html', product=product)


if __name__ == '__main__':
    app.run()
