from flask import Blueprint, render_template

products = Blueprint('products', __name__)

@products.route('/cart')
def dash():
    return render_template('cart.html')


@products.route('/')
def home():
    return render_template('index.html')