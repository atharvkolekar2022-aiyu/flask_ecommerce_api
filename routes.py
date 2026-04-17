from flask import request, jsonify, render_template
import service


def register_routes(app):
    """Register all application routes"""
    
    # Serve the frontend
    @app.route('/')
    def index():
        """Serve the main frontend page"""
        return render_template('index.html')

    # ==================== PRODUCT ROUTES ====================
    
    @app.route('/api/products', methods=['GET'])
    def get_products():
        """
        Get all products
        ---
        responses:
          200:
            description: List of all products
            schema:
              type: array
              items:
                properties:
                  id:
                    type: integer
                  name:
                    type: string
                  price:
                    type: number
                  description:
                    type: string
                  quantity:
                    type: integer
        """
        products = service.get_all_products()
        return jsonify(products)

    @app.route('/api/products/<int:product_id>', methods=['GET'])
    def get_product(product_id):
        """
        Get a specific product by ID
        ---
        parameters:
          - name: product_id
            in: path
            type: integer
            required: true
        responses:
          200:
            description: Product details
          404:
            description: Product not found
        """
        product = service.get_product_by_id(product_id)
        if product:
            return jsonify(product)
        else:
            return jsonify({'error': 'Product not found'}), 404

    @app.route('/api/products', methods=['POST'])
    def create_product():
        """
        Create a new product
        ---
        parameters:
          - name: body
            in: body
            required: true
            schema:
              properties:
                name:
                  type: string
                  description: Product name
                price:
                  type: number
                  description: Product price
                description:
                  type: string
                  description: Product description (optional)
                quantity:
                  type: integer
                  description: Stock quantity (optional)
        responses:
          201:
            description: Product created successfully
          400:
            description: Missing required fields
        """
        data = request.get_json()
        
        # Validate incoming data
        if not data or 'name' not in data or 'price' not in data:
            return jsonify({'error': 'Missing required fields: name and price'}), 400
        
        result, status = service.create_product(
            name=data['name'],
            price=data['price'],
            description=data.get('description'),
            quantity=data.get('quantity', 0)
        )
        return jsonify(result), status

    @app.route('/api/products/<int:product_id>', methods=['PUT'])
    def update_product(product_id):
        """
        Update an existing product
        ---
        parameters:
          - name: product_id
            in: path
            type: integer
            required: true
          - name: body
            in: body
            schema:
              properties:
                name:
                  type: string
                price:
                  type: number
                description:
                  type: string
                quantity:
                  type: integer
        responses:
          200:
            description: Product updated successfully
          404:
            description: Product not found
        """
        data = request.get_json()
        result, status = service.update_product(
            product_id,
            name=data.get('name'),
            price=data.get('price'),
            description=data.get('description'),
            quantity=data.get('quantity')
        )
        return jsonify(result), status

    @app.route('/api/products/<int:product_id>', methods=['DELETE'])
    def delete_product(product_id):
        """
        Delete a product
        ---
        parameters:
          - name: product_id
            in: path
            type: integer
            required: true
        responses:
          200:
            description: Product deleted successfully
          404:
            description: Product not found
        """
        result, status = service.delete_product(product_id)
        return jsonify(result), status

    # ==================== SEARCH ROUTES ====================
    
    @app.route('/search', methods=['GET'])
    def search():
        """
        Search products by name
        ---
        parameters:
          - name: q
            in: query
            type: string
            required: false
            description: Search query
          - name: limit
            in: query
            type: integer
            required: false
            description: Maximum number of results
        responses:
          200:
            description: Search results
            schema:
              properties:
                query:
                  type: string
                limit:
                  type: integer
                results:
                  type: array
        """
        query = request.args.get('q', '')
        limit = request.args.get('limit', 10, type=int)
        
        results = service.search_products(query, limit)
        return jsonify({
            'query': query,
            'limit': limit,
            'results': results
        })
