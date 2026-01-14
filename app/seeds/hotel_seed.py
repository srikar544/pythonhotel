from sqlalchemy import text
from app import create_app, db
from app.models import Hotel, Room
from random import choice, randint

app = create_app()

with app.app_context():

    # Clear existing data
    Room.query.delete()
    Hotel.query.delete()
    db.session.commit()

    db.session.execute(text("ALTER TABLE hotel AUTO_INCREMENT = 1;"))
    db.session.execute(text("ALTER TABLE room AUTO_INCREMENT = 1;"))
    db.session.commit()


    # Sample data
    hotel_names = [
        "Grand Palace", "Ocean View", "City Inn", "Royal Suites", "Sunshine Hotel",
        "Mountain Retreat", "Lakefront Lodge", "Elite Stay", "Comfort Inn", "The Horizon"
    ]
    cities = ["Mumbai", "Goa", "Delhi", "Bangalore", "Chennai", "Kolkata", "Jaipur", "Pune", "Hyderabad", "Lucknow"]
    room_types = ["Single", "Double", "Suite"]

    hotels = []

    # Create 10 hotels with 2 rooms each
    for i in range(10):
        hotel = Hotel(
            name=hotel_names[i],
            city=cities[i],
            address=f"{randint(100,999)} {cities[i]} Street"
        )
        db.session.add(hotel)
        db.session.commit()  # hotel.id exists
        hotels.append(hotel)

        # Create 2 rooms per hotel
        num_rooms = randint(1,5)
        for j in range(num_rooms):
            if hotel_names[i] in ["Grand Palace","Royal Suites","Elite Stay"]:
               price= randint(5000,8000) #Premium Hotels
            elif hotel_names[i] in ["Ocean View", "Sunshine Hotel", "Lakefront Lodge"]:
               price  = randint(3000, 6000)  # mid-range
            else:
                price = randint(1500,3500) # budget hotels

            room = Room(
                hotel_id=hotel.id,
                room_number=f"{101+j}",  # 101, 102 for each hotel
                room_type=choice(room_types),
                price=price
            )
            db.session.add(room)

        db.session.commit()  # commit rooms for this hotel

    print("10 Hotels and 20 Rooms Seeded successfully!")
