from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

# =========================
# USER MODEL
# =========================
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique user ID
    email = db.Column(db.String(120), unique=True, nullable=False)  # Unique email
    password_hash = db.Column(db.String(256), nullable=False)       # Hashed password
    role = db.Column(db.String(20), default="USER")                # User role (USER / ADMIN)
    username = db.Column(db.String(80), unique=True, nullable=False)  # Username
    bookings = db.relationship("Booking", backref="user", lazy=True)  # One-to-many: User -> Bookings

    # Hash and store password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check password validity
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# =========================
# HOTEL MODEL
# =========================
class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique hotel ID
    name = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(256))
    rooms = db.relationship("Room", backref="hotel", lazy=True)  # One-to-many: Hotel -> Rooms


# =========================
# ROOM MODEL
# =========================
class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)  # Link to Hotel
    room_number = db.Column(db.String(10), nullable=False)  # Room number e.g., "101"
    room_type = db.Column(db.String(50))                   # Type: Single, Double, Suite
    price = db.Column(db.Float, nullable=False)           # Price per night
    bookings = db.relationship("Booking", backref="room", lazy=True)  # One-to-many: Room -> Bookings


# =========================
# BOOKING MODEL
# =========================
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # Link to User
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)  # Link to Room

    check_in = db.Column(db.Date, nullable=False)   # Check-in date
    check_out = db.Column(db.Date, nullable=False)  # Check-out date

    status = db.Column(db.String(20), default="CONFIRMED")  # Booking status: CONFIRMED / CANCELLED
    canceled_at = db.Column(db.DateTime)                     # Timestamp when cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Booking creation timestamp
