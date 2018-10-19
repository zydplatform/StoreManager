from flask import jsonify,request

import unittest

import json

import sys

sys.path.append("../..")

class StoreApiTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.request_data={
            "product_id":1,
            "product_name":"Shirt",
            "product_price":15000, #@ shirt costs 15000
            "product_quantity" : 200,
            "minimum_amount" : 120
        }
        self.Saleorder={
            "sale_id": 1,
            "product_name":"Shirt",
            "product_price" : 150000,
            "product_quantity" : 10,
            "Attendant":"attendant1",
            "product_category" : "Office Wear"
        }
        self.user={
            "name" :"admin",
            "password" : "admin"
        }
    # store manager users login tests
    def test_addUser(self):
        response = self.test_client.post('/api/v1/users/owner/<string:name>',
        data=json.dumps(self.request_data),content_type='application/json')
        self.assertEqual(response.status,200)

    # only owner adds new product to inventory
    def test_productAddition(self):
        response = self.test_client.post(
            '/api/v1/owner/products', data=json.dumps(self.request_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)

        self.assertIn(
            'New product Added', str(response.data)
        )

    # attendants cannot add new product to inventory 
    def test_productAttendants(self):
        response = self.test_client.post(
        '/api/v1/products', data=json.dumps(self.request_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,405)
        
    #fetching all products and product details in stock
    def test_getProducts(self):
        response = self.test_client.get( 
            '/api/v1/products', data=json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)

    #fetching a single products and product details in stock
    def test_getSingleproduct(self):
        response=self.test_client.post(
            'api/v1/owner/products', data=json.dumps(self.request_data), content_type = 'application/json')
        response = self.test_client.get(
            '/api/v1/products/1',  content_type='application/json')
        self.assertEqual(response.status_code,200)
        

    #only a store attendants can create sales
    def test_CreateSaleorder(self):    
        response = self.test_client.post(
            '/api/v1/attendant/sales', data=json.dumps(self.sale_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        self.assertIn(
            'Sale order created', str(response.data)
        )

    #fetch all sale order records
    def test_Allsaleorders(self):
        response = self.test_client.get( 
            '/api/v1/owner/sales', data=json.dumps(self.sale_data), content_type = 'application/json')
        self.assertEqual(response.status_code,200)



    #fetch specific sale order record    
    def test_getSpecificsaleorder(self):
        response = self.test_client.get(
            '/api/v1/sales/1', data=json.dumps(self.sale_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
    
    if __name__ == "__main__":
        unittest.main()