from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configurations from config file
    app.config.from_pyfile('instance/config.py')

    # Initialize the database
    db.init_app(app)

    # Register Blueprint
    from .routes import main
    app.register_blueprint(main)

    return app
