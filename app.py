from flask import Flask
from models import db, bcrypt
from api import api
from views import products
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

Migrate(app=app, db=db)

app.register_blueprint(products, url_prefix='/')

with app.app_context():
    db.init_app(app)
    db.create_all()
    bcrypt.init_app(app)
    api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
