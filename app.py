from flask import Flask
from models import db, bcrypt
from api import api
from views import dash

app = Flask(__name__)

app.register_blueprint(dash, url_prefix='/')

with app.app_context():
    db.create_all()
    db.init_app(app)
    bcrypt.init_app(app)
    api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=4501)
