from flask import Flask
from databases import db, Ingredient, Product, Stock

app = Flask (__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stock.db"

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)