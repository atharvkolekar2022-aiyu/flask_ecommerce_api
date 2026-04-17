from db import db, Product

# GET OPERATIONS
def get_all_products():
    """Get all products from database"""
    products = Product.query.all()
    return [product.to_dict() for product in products]

def get_product_by_id(product_id):
    """Get a specific product by ID"""
    product = Product.query.get(product_id)
    return product.to_dict() if product else None

def search_products(query, limit=10):
    """Search products by name"""
    products = Product.query.filter(
        Product.name.ilike(f'%{query}%')
    ).limit(limit).all()
    return [product.to_dict() for product in products]

# CREATE OPERATIONS
def create_product(name, price, description=None, quantity=0):
    """Create a new product"""
    product = Product(
        name=name,
        price=price,
        description=description,
        quantity=quantity
    )
    try:
        db.session.add(product)
        db.session.commit()
        return product.to_dict(), 201
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

# UPDATE OPERATIONS
def update_product(product_id, name=None, price=None, description=None, quantity=None):
    """Update an existing product"""
    product = Product.query.get(product_id)
    
    if not product:
        return {'error': 'Product not found'}, 404
    
    try:
        if name is not None:
            product.name = name
        if price is not None:
            product.price = price
        if description is not None:
            product.description = description
        if quantity is not None:
            product.quantity = quantity
        
        db.session.commit()
        return product.to_dict(), 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400

# DELETE OPERATIONS
def delete_product(product_id):
    """Delete a product by ID"""
    product = Product.query.get(product_id)
    
    if not product:
        return {'error': 'Product not found'}, 404
    
    try:
        db.session.delete(product)
        db.session.commit()
        return {'message': f'Product {product_id} deleted successfully'}, 200
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 400
