from datetime import date, datetime
from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for
from app.models import Booking, Hotel, Room, User
from app import db

# =========================
# Blueprint
# =========================
health_bp = Blueprint("health", __name__, url_prefix="")

# =========================
# Home Page
# =========================
@health_bp.route("/", methods=["GET"])
def home():
    # Public homepage
    return render_template("index.html")

# =========================
# Registration Page
# =========================
@health_bp.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")

# =========================
# Login Page
# =========================
@health_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

# =========================
# Hotels List (Protected)
# =========================
@health_bp.route("/hotels", methods=["GET"])
def hotels():
    if "user_id" not in session:
        return redirect(url_for("health.login_page"))
    
    # Fetch all hotels and rooms
    hotels = Hotel.query.order_by(Hotel.id).all()
    
    return render_template("hotels.html", hotels=hotels)

# =========================
# API: User Registration
# =========================
@health_bp.route("/api/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return redirect(url_for("health.register_page"))
    
    data = request.get_json()
    
    # Validate input
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400
    
    # Check for existing user
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "User already exists"}), 409
    
    # Create new user
    user = User(email=data["email"])
    user.set_password(data["password"])
    
    db.session.add(user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully", "user_id": user.id}), 201

# =========================
# API: User Login
# =========================
@health_bp.route("/api/login", methods=["GET","POST"])
def login_api():
    if request.method == "GET":
        return render_template("login.html")
    
    data = request.get_json()
    
    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Email and password required"}), 400
    
    user = User.query.filter_by(email=data["email"]).first()
    
    if not user or not user.check_password(data["password"]):
        return jsonify({"error": "Invalid email or password"}), 400
    
    # Set session
    session['user_id'] = user.id
    session['username'] = user.username
    
    return jsonify({"message": "Login Successfull", "user_id": user.id}), 200

# =========================
# Logout
# =========================
@health_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("health.home"))

# =========================
# Book a Room (GET → show form, POST → save booking)
# =========================
@health_bp.route("/book/<int:room_id>", methods=["GET", "POST"])
def book_room(room_id):
    if "user_id" not in session:
        return redirect(url_for("health.login_page"))
    
    room = Room.query.get_or_404(room_id)

    # Fetch existing confirmed bookings for this room to disable dates
    bookings = Booking.query.filter(
        Booking.room_id == room.id,
        Booking.status == "CONFIRMED"
    ).all()
    
    # Prepare disabled date ranges for frontend
    disabled_ranges = [
        {
            "check_in": b.check_in.strftime("%Y-%m-%d"),
            "check_out": b.check_out.strftime("%Y-%m-%d")
        }
        for b in bookings
    ]

    # -------------------
    # POST → Confirm Booking
    # -------------------
    if request.method == "POST":
        check_in_str = request.form.get("check_in")
        check_out_str = request.form.get("check_out")
        
        # Convert string to date
        check_in = datetime.strptime(check_in_str, "%Y-%m-%d").date()
        check_out = datetime.strptime(check_out_str, "%Y-%m-%d").date()

        nights = (check_out - check_in).days
        if nights <= 0:
            return "Invalid date range"

        # Prevent overlapping bookings
        conflict = Booking.query.filter(
            Booking.room_id == room.id,
            Booking.status == "CONFIRMED",
            Booking.check_in < check_out,
            Booking.check_out > check_in
        ).first()
        if conflict:
            return "Room already booked for selected dates"

        total_price = nights * room.price

        # Save booking
        booking = Booking(
            user_id=session["user_id"],
            room_id=room.id,
            check_in=check_in,
            check_out=check_out,
            status="CONFIRMED"
        )
        db.session.add(booking)
        db.session.commit()

        return render_template(
            "booking_success.html",
            room=room,
            nights=nights,
            total_price=total_price
        )

    # -------------------
    # GET → Show booking form
    # -------------------
    return render_template("book.html", room=room, disabled_ranges=disabled_ranges)

# =========================
# My Bookings Page
# =========================
@health_bp.route("/my-bookings")
def mybookings():
    if "user_id" not in session:
        return redirect(url_for("health.login_page"))

    today = date.today()

    # Fetch confirmed bookings that are not past
    bookings = Booking.query.filter(
        Booking.user_id == session["user_id"],
        Booking.status == "CONFIRMED",
        Booking.check_out >= today  # Only future or ongoing bookings
    ).order_by(Booking.check_in.asc()).all()

    return render_template("my_bookings.html", bookings=bookings, today=today)

# =========================
# Cancel a Booking
# =========================
@health_bp.route("/cancel-booking/<int:booking_id>", methods=["POST"])
def cancel_booking(booking_id):
    if "user_id" not in session:
        return redirect(url_for("health.login_page"))
    
    booking = Booking.query.get_or_404(booking_id)

    # Security check → only booking owner can cancel
    if booking.user_id != session["user_id"]:
        return "UnAuthorized", 403

    # Prevent cancelling past or ongoing bookings
    if booking.check_in <= date.today():
        return "Cannot cancel past or ongoing booking"

    booking.status = "CANCELLED"
    booking.canceled_at = datetime.utcnow()

    db.session.commit()

    # Return success (AJAX handler removes card)
    return redirect(url_for("health.mybookings"))
