from flask import Flask
from app.models.customer_model import Customer
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.status_codes import HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_200_OK,HTTP_401_UNAUTHORIZED

from datetime import datetime
customer = Blueprint("customer", __name__, url_prefix='/api/v1/customer')



@customer.route('/register', methods=['POST'])
def register_product():
    data = request.get_json()
    customer_id=data.get("customer_id")
    name = data.get("name")
    address=data.get("address")
    location=data.get("location")
    email=data.get("emai")
    contact=data.get("contact")
    
    #Validators
    if not customer_id or not name or not address or not location or not email or not contact:
       return jsonify({"error":"Fields are all required"})
   
   
   
    