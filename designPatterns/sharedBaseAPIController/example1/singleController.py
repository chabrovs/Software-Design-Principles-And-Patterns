from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    if user_id <= 0:
        return jsonify({"error": "Invalid User ID"}), 400
    
    try:
        user = {"id": user_id, "name": "Sergei"}
        return jsonify({"status": "success", "data": user})
    except Exception as e:
        return jsonify({"error": str(e)}), 500 
    
@app.route("/product/<int:user_id>", methods=["GET"])
def get_product(product_id):
    if product_id <= 0:
        return jsonify({"error": "Invalid Product ID"}), 400
    try:
        product = {"id": product_id, "name": "Product1"}
        return jsonify({"status": "success", "product": product})
    except Exception as e:
        return jsonify({"error": str(e)}), 500 
        

if __name__ == "__main__":
    app.run(debug=True)


# This module contains duplicated login in both controllers \
# 'get_user' and 'get_product'. 