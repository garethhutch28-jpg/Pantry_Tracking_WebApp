from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#ingredients for recepies
class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000),unique=True, nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    products = db.relationship("Product", back_populates="ingredient")

#Products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    brand = db.Column(db.String(1000), nullable = False)
    name = db.Column(db.String(1000))
    barcode = db.Column(db.String(40),unique=True, nullable = True)
    size = db.Column(db.Float)
    pack_count = db.Column(db.Integer)
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredient.id"), nullable=False)
    ingredient = db.relationship("Ingredient", back_populates="products")
    stock = db.relationship("Stock", back_populates="product")

#actual things in the cupboard and fridge
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    expiry_date = db.Column(db.Date, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"),nullable = False)
    pack_remaining = db.Column(db.Float, nullable=False)
    product = db.relationship("Product", back_populates="stock")


