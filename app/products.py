from flask import Flask

from flask_restful import Api,Resource,reqparse

from app import app

api = Api(app)

products = [{
                "product_name":"shirt",
                "product_id":1,
                "product_price":15000,
                "product_quantity":100
            },
            {
                "product_name":"shoes",
                "product_id":2,
                "product_price":6000,
                "product_quantity":79

            },
            {
                "product_name":"coat",
                "product_id":3,
                "product_price":45000,
                "product_quantity":10

            }
           ]
'''
 Creating our API endpoints by defining a Product resource class.
let us use the four functions :get,post,put,delete
'''


class Product(Resource):
    #retrieving product details:
    def get(self,product_name):
        for product in products:
            if(product_name == product['product_name']):
                return product,200
           
        return 'product not found ',404 #status code not found

    #adding new product in store:
    def post(self,product_name):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id')
        parser.add_argument('product_price')
        parser.add_argument('product_quantity')
        args = parser.parse_args()

        for product in products:
            if(product_name == product['name']):
                return 'product with product_name {} already exists'.format(product_name),400 #status code bad request

        product = {
                'product_name': product_name,
                'product_id': args['product_id'],
                'product_price': args['product_price'],
                'product_quantity': args['product_price']
        }
        products.append(product)
        return product,201 #status code product created
    '''
    The post method is used to create a new product:
    '''
    def put(self,product_name):
        parser = reqparse.RequestParser()
        parser.add_argument('product_id')
        parser.add_argument('product_price')
        parser.add_argument('product_quantity')
        args = parser.parse_args()
        
        for product in products:
            if(product_name == product['product_name']):
                product['product_id'] = args['product_id']
                product['product_price'] = args['product_price']
                product['product_quantity'] = args['product_quantity']
                return product,200

        product = {
                    'product_name': product_name,
                    'product_id': args['product_id'],
                    'product_price': args['product_price'],
                    'product_quantity': args['product_quantity']
        }
        products.append(product)
        return product,201

    def delete(self,product_name):
        global products
        products = [product for product in products if product['product_name'] != product_name]
        return "{} is deleted .".format(product_name), 200

api.add_resource(Product,"/api/v1/product/<string:product_name>")

class Allproducts(Resource):
    def get(self):
        return products,200

api.add_resource(Allproducts,"/api/v1/products")
class Index(Resource):
  def index(self):
    return products,200
api.add_resource(Index,"/")

