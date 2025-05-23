from flask import Flask
from app.extensions import db
from datetime import datetime

class Product(db.Model):
    __tablename__="Product"
    id= db.Column(db.Integer,Primary_key=True,auto_increment=True,nullable=False)
    name=db.Column(db.String(225),nullable=False)
    price=db.Column(db.String(225),nullable=False)
    category=db.Column(db.String(225),Foreign_Key=True, nullable=False)
    expiry_date=db.Column(db.String(50),nullable=False)

    
    def product_name(name):
        return f"The product name is{name}"

