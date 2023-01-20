from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "Pues te pego un tiro!"})

@app.route('/products')
def getProducts():
    return jsonify({"products": products, "message": "List of products"})

@app.route('/products/<product_name>')
def getProduct(product_name):
    productFound=[product for product in products if product['product'] == product_name]
    if (len(productFound) > 0):
        return jsonify({"product": productFound[0]})
    return jsonify({"message": "Product Not Found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product= {
        "name": request.json['name'],
        "price": request.json['price'], 
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    print(request.json)
    return jsonify({"message": "Product Added Successfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound= [product for product in products if product['product'] == product_name]
    if(len(productFound) > 0):
        productFound[0]['product']= request.json['product']
        productFound[0]['quantity']= request.json['quantity']
        productFound[0]['price']= request.json['price']
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product Not Found"})


@app.route('/products/<string:product_name>', methods= ['DELETE'])
def deleteProduct(product_name):
        productFound=[product for product in products if product['product'] == product_name]
        if(len(productFound) > 0):
            products.remove(productFound[0])
            return jsonify({
                "message": "Product Deleted",
                "products": products
            })
        return jsonify({"message": "Product Not Found"})

if __name__ == 'main':
    app.run()

