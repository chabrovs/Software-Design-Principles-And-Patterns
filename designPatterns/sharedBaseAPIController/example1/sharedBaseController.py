from flask import Flask, jsonify, request


app = Flask(__name__)


class BaseController:
    """A shared base controller for handling common API logic."""

    def validate_id(self, entity_id):
        """Validate that the entity id is a positive integer"""

        if entity_id <= 0:
            return self.self.error_response("Invalid ID", 400)
        
        return None
    
    def success_response(self, data):
        """Formats a successful response."""

        return jsonify({"status": "success", "data": data})
    
    def error_response(self, message, status_code=500):
        """Formats an error response."""
        return jsonify({"status": "error", "message": message}), status_code
    

# Inherit from the Base Controller.
class UserController(BaseController):
    def get_user(self, user_id: int):
        """Handles fetching a user by ID."""
        validation_error = self.validate_id(user_id)
        
        if validation_error:
            return validation_error

        try:
            user = {"id": user_id, "name": "Sergei"}
            return self.success_response(user)        
        except Exception as e:
            return self.error_response(str(e))


class ProductController(BaseController):
    def get_product(self, product_id: int):
        """Handles fetching a user by ID."""
        validation_error = self.validate_id(product_id)
        
        if validation_error:
            return validation_error

        try:
            product = {"id": product_id, "name": "Product1"}
            return self.success_response(product)        
        except Exception as e:
            return self.error_response(str(e))
    

user_controller = UserController()
product_controller = ProductController()

@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return user_controller.get_user(user_id)

@app.route("/product/<int:product_id>", methods=["GET"])
def get_product(product_id):
    return product_controller.get_product(product_id)


if __name__ == "__main__":
    app.run(debug=True)
