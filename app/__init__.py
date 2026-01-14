# Import necessary libraries
from urllib.parse import quote_plus        # Used to safely encode DB passwords with special characters
from dotenv import load_dotenv             # Load environment variables from a .env file
from flask import Flask                     # Flask framework
from flask_sqlalchemy import SQLAlchemy     # ORM for database interactions
import os                                   # To access environment variables

# Initialize SQLAlchemy (DB instance)
db = SQLAlchemy()

def create_app():
    """
    Factory function to create and configure a Flask app instance.
    """
    app = Flask(__name__)  # Create Flask app instance

    # Load environment variables from .env file
    load_dotenv()

    # Get database connection details from environment variables
    user = os.getenv("DB_USER")
    password = quote_plus(os.getenv("DB_PASSWORD"))  # Encode password safely for URL
    host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")

    # Set a secret key for session management, default if not in .env
    app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")

    # Configure SQLAlchemy database URI for MySQL
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+mysqlconnector://{user}:{password}@{host}/{db_name}"
    )
    # Disable modification tracking (saves memory)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize SQLAlchemy with the app
    db.init_app(app)

    # Import and register blueprints (modular routing)
    from app.routes import health_bp
    app.register_blueprint(health_bp)

    # Create database tables if they don't exist (requires app context)
    with app.app_context():
        db.create_all()

    return app  # Return the configured Flask app
