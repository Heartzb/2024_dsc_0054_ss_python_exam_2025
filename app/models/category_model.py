from flask import Flask
from app.extensions import db
from datetime import datetime

class Category(db.model):
    __Table__="Category"
    
category_id=db.Column(db.Integer,Primary_key=True,auto_increment=True,nullable=False)  
name=db.olumn(db.String(225),nullable=False)


def category_name(name):
        return f"The category name is{name}"
