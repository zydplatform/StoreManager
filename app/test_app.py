import json
from flask import jsonify
import unittest
from app import app
class StoreApiTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.request_data={
                            "product_id":1,
                            "product_name":"shirt",
                            "product_price":15000,
                            "product_quantity" : 20
                          }
        self.sale_data ={
                             "sale_made_by":"attendant1",
                             "sale_id":1,
                             "Total_worth_products_sold":120000,
                             "Products_sold_total":150
                        }
        self.user_data ={
                            "username":"admin",
                            "password":"admin"
                        }

    def test_addProduct(self):
        response = self.test_client.post(
            '/api/v1/product/',
             data=json.dumps(self.request_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        # self.assertIn(
        #     'Product added', str(response.data))
    def test_addTocart(self,product_name):
        response = self.test_client.post(
        '/api/v1/product/<string:product_name>', data=json.dumps(self.request_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,405)
        
    def test_getProducts(self):
        response = self.test_client.get( 
            '/api/v1/products', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)
    
    def test_getProduct(self,product_name):
        response=self.test_client.post(
            '/api/v1/product/<string:product_name>', data=json.dumps(self.request_data), content_type = 'application/json')
        response = self.test_client.get(
            '/api/v1/product/<string:product_name>',  content_type='application/json')
        self.assertEqual(response.status_code,200)
    #tests for sales :

    def test_addSaleorder(self,sale_id):    
        response = self.test_client.post(
            '/api/v1/sale/<int:sale_id>', data=json.dumps(self.sale_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        # self.assertIn(
        #     'You have successfully created a sale order', str(response.data)
        # )
    def test_getSinglesaleorder(self,sale_id):
        response = self.test_client.get(
            '/api/v1/sale/shirt', data=json.dumps(self.sale_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)

    def test_getAllsaleorders(self):
        response = self.test_client.get( 
            '/api/v1/sales', data=json.dumps(self.sale_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)

    def test_getUser(self,username):
        response = self.test_client.get('/api/v1/user/attendant',data=json.dumps(self.user_data),
        content_type='application/json')
        self.assertEqual(response.status_code,200)

    def test_getUsers(self):
        response = self.test_client.get('/api/v1/users',data=json.dumps(self.user_data),
        content_type='application/json')
        self.assertEqual(response.status_code,200)
    
    def test_addUser(self,username):
        response = self.test_client.get('/api/v1/user/attendant',data=json.dumps(self.user_data),
        content_type='application/json')
        self.assertEqual(response.status_code,200)
    
# if __name__ == "__main__":
#     unittest.main()