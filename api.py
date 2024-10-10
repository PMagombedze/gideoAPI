from flask_restful import Api, reqparse, Resource
from models import Product
from flask import jsonify

api = Api()

class ProductList(Resource):
    def get(self):
        products = Product.query.all()
        return jsonify([product.to_dict() for product in products])

class ProductResource(Resource):
    def get(self, id):
        product = Product.query.get(id)
        if product:
            return jsonify(product.to_dict())
        return {'message': 'Product not found'}, 404

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help="Name cannot be blank!")
        parser.add_argument('price', type=float, required=True, help="Price cannot be blank!")
        data = parser.parse_args()

        product = Product.query.get(id)
        if product:
            product.name = data['name']
            product.price = data['price']
            product.save()
            return jsonify(product.to_dict())
        return {'message': 'Product not found'}, 404

    def delete(self, id):
        product = Product.query.get(id)
        if product:
            product.delete()
            return {'message': 'Product deleted'}
        return {'message': 'Product not found'}, 404

api.add_resource(ProductList, '/api/products')
api.add_resource(ProductResource, '/api/products/<string:id>')
