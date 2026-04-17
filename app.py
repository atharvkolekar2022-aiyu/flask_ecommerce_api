from flask import Flask
from flasgger import Swagger
from db import init_db
from routes import register_routes


def create_app():
    """Application factory function"""
    # Create Flask app
    app = Flask(__name__)
    
    # Initialize Swagger for API documentation
    Swagger(app)
    
    # Initialize Database
    init_db(app)
    
    # Enable CORS for frontend requests
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    
    # Register all routes
    register_routes(app)
    
    return app


# Create and run the app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
