from flask import Flask
from app.models.category_model import Category
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_200_OK,HTTP_401_UNAUTHORIZED
import validators
from datetime import datetime
Category = Blueprint("category", __name__, url_prefix='/api/v1/Category')
@Category.route('/register', methods=['POST'])
def register_product():
    data = request.get_json()
    Category_id=data.get("id")
    name = data.get("name")
    
    if not Category_id or not name :
        return jsonify({"error": "All fields are required"}),HTTP_400_BAD_REQUEST
    if Category.query.filter_by(Category_id=Category_id).first() is not None:
        return jsonify({'error':"Category already registered"}),HTTP_409_CONFLICT
    
    


