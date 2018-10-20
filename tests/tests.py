import json
from flask import jsonify




# from api.resources import app
# from storeapi.models import Product, products
import unittest

class StoreApiTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.request_data={
            "product_id":1,
            "product_ame":"Foam",
            "product_rice":3000
        }
        self.sale_data={
            "saleId":'1',
            "productName":"Foam",
            "created_by":"myself",
            "details":"Mattress material"
        }

    def test_addProduct(self):
        response = self.test_client.post(
            '/api/v1/owner/products', data=json.dumps(self.request_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        self.assertIn(
            'Product added', str(response.data)
        )
    def test_addByattendant(self):
        response = self.test_client.post(
        '/api/v1/products', data=json.dumps(self.request_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,405)
        
    def test_getProducts(self):
        response = self.test_client.get( 
            '/api/v1/products', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)
    
    def test_getProduct(self):
        response=self.test_client.post(
            'api/va/owner/products', data=json.dumps(self.request_data), content_type = 'application/json')
        response = self.test_client.get(
            '/api/v1/products/1',  content_type='application/json')
        self.assertEqual(response.status_code,200)
        


    def test_addSaleorder(self):    
        response = self.test_client.post(
            '/api/v1/attendant/sales', data=json.dumps(self.sale_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        self.assertIn(
            'You have successfully created a sale order', str(response.data)
        )
    def test_getSinglesaleorder(self):
        response = self.test_client.get(
            '/api/v1/sales/1', data=json.dumps(self.sale_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)

    def test_getAllsaleorders(self):
        response = self.test_client.get( 
            '/api/v1/owner/sales', data=json.dumps(self.sale_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)
    
if __name__ == "__main__":
    unittest.main()