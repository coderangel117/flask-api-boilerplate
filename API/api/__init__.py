from api.config import Config
from api.extensions import db, migrate, bcrypt
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    register(app)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    # from api.model import author_model
    return app


def register(app):
    pass
    # from api.route import author_bp

    # app.register_blueprint(author_bp)
