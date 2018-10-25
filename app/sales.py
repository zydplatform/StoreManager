from flask import Flask

from flask_restful import Api,Resource,reqparse

from run import app

app.config['DEBUG'] =True

api = Api(app)

sales =[{
            "sale_made_by":"attendant1",
            "sale_id":1,
            "Total_worth_products_sold":120000,
            "Products_sold_total":150
        },
        {
            "sale_made_by":"attendant2",
            "sale_id":2,
            "Total_worth_products_sold":800000,
            "Products_sold_total":550
        },
        {
            "sale_made_by":"attendant3",
            "sale_id":3,
            "Total_worth_products_sold":1020000,
            "Products_sold_total":1150
        }
       ]

class Sale(Resource):
    #get specific sale
    def get(self,sale_id):
        for sale in sales:
            if sale_id == sale['sale_id']:
                return sale,200

        return 'Sale not found',404

    def post(self,sale_id):
        parser = reqparse.RequestParser()
        parser.add_argument('sale_made_by')
        parser.add_argument('Total_worth_products_sold')
        parser.add_argument('Products_sold_total')        
        args = parser.parse_args()

        for sale in sales :
            if sale_id == sale['sale_id']:
                return 'Sale with sale_id {} already exists'.format(sale_id),400
        
        sale = {"sale_id":sale_id,
                "sale_made_by":args['sale_made_by'],
                "Total_worth_products_sold":args['Total_worth_products_sold'],
                "Products_sold_total":args['Products_sold_total']
               }
        sales.append(sale)
        return sale,201
    
    def put(self,sale_id):
        parser = reqparse.RequestParser()
        parser.add_argument('sale_made_by')
        parser.add_argument('Total_worth_products_sold')
        parser.add_argument('Products_sold_total')
        args = parser.parse_args()

        for sale in sales :
            if sale_id == sale['sale_id']:
                sale['sale_made_by'] = args['sale_made_by']
                sale['Total_worth_products_sold'] = args['Total_worth_products_sold']
                sale['Products_sold_total'] = args['Products_sold_total']
                return sale,200

        sale = {"sale_id":sale_id,
                "sale_made_by":args['sale_made_by'],
                "Total_worth_products_sold":args['Total_worth_products_sold'],
                "Products_sold_total":args['Products_sold_total']
               }
        sales.append(sale)
        return sale,201

    def delete(self,sale_id):
        global sales
        sales =[sale for sale in sales if sale['sale_id'] != sale_id]
        return '{} is deleted '.format(sale_id),200

api.add_resource(Sale,"/api/v1/sale/<int:sale_id>")

class Allsales(Resource):
    def get(self):
        return sales,200
api.add_resource(Allsales,"/api/v1/sales")

app.run(port=5000)