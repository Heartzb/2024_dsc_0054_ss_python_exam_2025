from flask import Flask
from app.extensions import db


class Customer(db.Model):
    __tablename__="Product"
    id= db.Column(db.Integer,Primary_key=True,auto_increment=True,nullable=False)
    name=db.Column(db.String(225),nullable=False)
    address=db.Column(db.String(225),nullable=False)
    location=db.Column(db.String(225), nullable=False)
    contact=db.Column(db.String(50),nullable=False)

    
    def customet_name(name):
        return f"The customer name is{name}"

