from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

# ---------------------------------------------------------
# Initialize Flask application
# ---------------------------------------------------------
# Required to access app config, database, and models
# outside the request/response cycle.
app = create_app()

# ---------------------------------------------------------
# Static user seed data
# ---------------------------------------------------------
# These users are created only if they do not already exist.
# Useful for demo, testing, and initial admin accounts.
users = [
    {"username": "admin", "email": "admin@hotel.com"},
    {"username": "john", "email": "john@hotel.com"},
    {"username": "alice", "email": "alice@hotel.com"},
    {"username": "bob", "email": "bob@hotel.com"},
    {"username": "mark", "email": "mark@hotel.com"},
    {"username": "linda", "email": "linda@hotel.com"},
    {"username": "steve", "email": "steve@hotel.com"},
    {"username": "nancy", "email": "nancy@hotel.com"},
    {"username": "paul", "email": "paul@hotel.com"},
    {"username": "emma", "email": "emma@hotel.com"},
]

with app.app_context():

    # -----------------------------------------------------
    # Loop through each predefined user
    # -----------------------------------------------------
    for u in users:

        # Check if user already exists (by unique email)
        exists = User.query.filter_by(email=u["email"]).first()

        if not exists:
            # Create new user only if not found
            user = User(
                username=u["username"],
                email=u["email"],
                password_hash=generate_password_hash("password123")
            )

            # Add new user to session
            db.session.add(user)

    # -----------------------------------------------------
    # Commit once after all users are added
    # -----------------------------------------------------
    # This is more efficient and avoids partial commits.
    db.session.commit()

    print("Seeded users successfully")
