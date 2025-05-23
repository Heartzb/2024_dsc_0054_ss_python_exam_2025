from flask import Flask
from app.models.product_model import Product
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_200_OK,HTTP_401_UNAUTHORIZED
import validators
from datetime import datetime
product = Blueprint("product", __name__, url_prefix='/api/v1/product')

@product.route('/register', methods=['POST'])
def register_product():
    data = request.get_json()
    id=data.get("id")
    name = data.get("name")
    price = data.get("price") 
    category = data.get("category")
    expiry_date = data.get("expiry_date")
    
    
    if not id or not name or not price or not category or not expiry_date:
        return jsonify({"error": "All fields are required"}),HTTP_400_BAD_REQUEST
    if Product.query.filter_by(name=name).first() is not None:
        return jsonify({'error':"product already registered"}),HTTP_409_CONFLICT
    
    try:
        expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Expiry date must be in YYYY-MM-DD format"}), HTTP_400_BAD_REQUEST

    
    
    try:
        new_product = Product(id=id, name=name,price=price,category=category,expiry_date=expiry_date)
        db.session.add(new_product)
        db.session.commit()
        
    
        
        return jsonify ({
            'message': new_product.name +   "   has been created" 
        }),HTTP_201_CREATED
    except Exception as e:
        db.session.rollback() 
        return jsonify({"error":str(e)}),HTTP_500_INTERNAL_SERVER_ERROR
        
@product.route('/', methods=['GET'])
def get_all_products():
    try:
        products = Product.query.all()

        if not products:
            return jsonify({'message': 'No products found'}), HTTP_200_OK

        product_list = []
        for product in products:
            product_list.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'category': product.category,
                'expiry_date': product.expiry_date.strftime('%Y-%m-%d'),
            })

        return jsonify(product_list), HTTP_200_OK

    except Exception as e:
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR


@product.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()

    try:
        product = Product.query.get(product_id)

        if not product:
            return jsonify({'error': 'Product not found'}), HTTP_400_BAD_REQUEST

        #  validation
        if 'name' in data:
            product.name = data['name']
        if 'price' in data:
            try:
                product.price = float(data['price'])
            except ValueError:
                return jsonify({'error': 'Price must be a number'}), HTTP_400_BAD_REQUEST
        
            
        if 'category' in data:
            product.category = data['category']
    

        if 'expiry_date' in data:
            from datetime import datetime
            try:
                product.expiry_date = datetime.strptime(data['expiry_date'], "%Y-%m-%d")
            except ValueError:
                return jsonify({'error': 'Expiry date must be in YYYY-MM-DD format'}), HTTP_400_BAD_REQUEST

        db.session.commit()

        return jsonify({
            'message': f"Product '{product.name}' updated successfully"
        }), HTTP_200_OK

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR


@product.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    try:
        product = Product.query.get(product_id)

        if not product:
            return jsonify({'error': 'Product not found'}), HTTP_400_BAD_REQUEST

        db.session.delete(product)
        db.session.commit()

        return jsonify({'message': f"Product '{product.name}' deleted successfully"}), HTTP_200_OK

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), HTTP_500_INTERNAL_SERVER_ERROR