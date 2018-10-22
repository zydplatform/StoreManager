from flask import Flask,json,request, jsonify

app= Flask(__name__)

app.config['DEBUG'] =True

products = []
specific_product = {}

class Product:
    def ___init__(self, product_id,product_name,product_price,product_quantity,minimum_amount,product_category):
        self.product_id=product_id
        self.product_name=product_name
        self.product_price=product_price
        self.product_quantity=product_quantity
        self.minimum_amount = minimum_amount

@app.route("/api/v1/owner/products", methods =["POST"])
def productAddition():
    request_data=request.get_json()
    product_id=len(products)+1
    product_name= request_data.get('product_name')
    product_price = request_data.get('product_price')
    product_category = request_data.get('product_category')
    product_quantity = request_data.get('product_quantity')
    minimum_amount = request_data.get('minimum_amount')

    if product_name == "": 
        return jsonify({"message":"Please insert a product name.."})
    
    elif product_name != type(str):
        return jsonify({"message":"Invalid product name.."})
        

    if product_price =="":
        return jsonify({'message':"Please insert price of a particular product"})

    elif product_price == type(str):
        return jsonify({"message":"Invalid value inserted"})

    addproduct={"product_id":product_id,"product_name":product_name,
    "product_price":product_price}
    products.append(addproduct)

    return jsonify({"message":'Product {product_name} successfully added'}),200

@app.route('/api/v1/products', methods=['GET'])
def getProducts():

    if len(products) >1:
        return jsonify({
            "message":"Available Products",
            "Products":products
        }),200
    
    return jsonify({"Error":"Products not found "})


@app.route('/api/v1/products/<int:product_id>',methods=['GET'])
def getSingleproduct(productId):
    if len(products) <1:
        return jsonify ({
            "Status":"Fail", 
            "message":"No products in inventory"
            }),404


    for specific_product in products:
        if specific_product['productId']==productId:
            return jsonify({
                "message":"You have fetched product",
                "Product":specific_product
            }),200

    return jsonify({
        "Error":"Product not found , check to see that you wrote the right ID"
        })

if __name__ == "__main__":
    app.run(port=5000)
