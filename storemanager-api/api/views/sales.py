from flask import Flask,json,request, jsonify

app= Flask(__name__)

app.config['DEBUG'] =True

saleorder_records = []
saleOrder = {}

class SaleRecord:
    def __init__(self, sale_id,product_name,Attendant,product_quantity,product_category):
        self.sale_id=sale_id
        self.product_name=product_name
        self.Attendant=Attendant
        self.product_quantity = product_quantity
        self.product_category = product_category

@app.route('/api/v1/attendant/sales',methods=['POST'])
def CreateSaleorder():
    sale_data=request.get_json()
    sale_id=len(saleorder_records)+1
    product_name=sale_data.get('product_name')
    Attendant=sale_data.get('Attendant')
    product_quantity =sale_data.get('product_quantity')

    newSales={'sale_id':sale_id, 'product_name':product_name, 'Attendant':Attendant,'product_quantity':product_quantity}
    saleorder_records.append(newSales)

    return jsonify({"message":"You have successfully created a sale order"}),200


@app.route('/api/v1/sales/<int:sale_id>', methods=['GET'])
def getSpecificsaleorder(sale_id):
    if len(saleorder_records)<1:
        return jsonify({
            "status":"Fail",
            "message":"NO sale orders at the moment"
        }),404

    
    for saleOrder in saleorder_records:
        if saleOrder['sale_id']==sale_id:
            return jsonify({
                "message":"You have fetched a sale order",
                "Sale_order":saleOrder
            }),200
    
    return jsonify({"Error":"Order not found , check to see that you wrote the right ID"})


@app.route('/api/v1/owner/sales', methods=['GET'])
def Allsaleorders():
    if len(saleorder_records) <1:
        return jsonify ({
            "status":"Fail",
            "message":"No sale orders at the moment"
        }),404

    if len(saleorder_records) >1:
        return jsonify({
            "message":"Sale orders",
            "Sales":saleorder_records
        }),200

    return jsonify({"Error":"Orders not found "})

if __name__ == "__main__":
    app.run(port=5000)
    

