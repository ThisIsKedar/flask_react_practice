from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__, template_folder='templates', static_folder='static')
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()

def create_app():
    """Application-factory pattern"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)

    return app