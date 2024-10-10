from flask import Blueprint, render_template

products = Blueprint('products', __name__)

@products.route('/products')
def dash():
    return render_template('products.html')
