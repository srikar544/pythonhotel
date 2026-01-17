🏨 Python Hotel Booking Platform

A Flask-based **Hotel Booking System** that allows users to browse available hotels and make bookings based on **real-time availability**.
The application follows a **production-ready, modular architecture**, supports **multiple concurrent users**, and is designed to be **scalable on AWS**. It emphasizes performance, security, and future extensibility.

##  Tech Stack

| **Layer**      | **Technology**          |
| -------------- | ----------------------- |
| Backend        | Flask                   |
| ORM            | Flask-SQLAlchemy        |
| Database       | MySQL                   |
| Authentication | Flask-Login             |
| Templates      | Jinja2                  |
| Styling        | HTML / CSS (Extendable) |

##  Application Features

* User registration functionality for new users.
* Secure login for existing users.
* Hotel booking based on real-time room availability.
* Prevention of double booking by restricting reservations when rooms are unavailable, even if multiple users attempt to book the same hotel simultaneously.

## Database Schema

| **Table** | **Primary Key** | **Foreign Keys** |
| --------- | --------------- | ---------------- |
| User      | id              | —                |
| Hotel     | id              | —                |
| Room      | id              | hotel_id         |
| Booking   | id              | user_id, room_id |

### Table Relationships

* `booking.user_id` → `user.id`
* `booking.room_id` → `room.id`
* `room.hotel_id` → `hotel.id`

###  Example Query

```sql
SELECT *
FROM user u
INNER JOIN booking b ON u.id = b.user_id
INNER JOIN room r ON r.id = b.room_id;
```
##  Application Flow

* On the **Home page**, users can either **register** or **log in**.
* If a user clicks **View Hotels** without logging in, they are redirected to the **Login page**.
* After successful login, clicking **View Hotels** loads all hotels from the database.
* When a user books a hotel, the user is mapped to the selected hotel and room in the **Bookings** table.

---

##  Screenshots

Home Page

<img width="1898" height="916" alt="image" src="https://github.com/user-attachments/assets/d5d42b27-65e4-4a15-a148-e13fa1295cb7" />

Click on My Bookings

<img width="1898" height="903" alt="image" src="https://github.com/user-attachments/assets/1198172f-c791-460c-b9a3-d6b2298a299a" />

Clicking on View Hotels link

<img width="1912" height="908" alt="image" src="https://github.com/user-attachments/assets/0f12a678-1810-4dbc-9dd5-1a03e93b4916" />

Clicking on Book button

<img width="1891" height="867" alt="image" src="https://github.com/user-attachments/assets/13323040-dac1-4225-9b27-47815c74b738" />

Navigates to the Confirm Booking Screen

<img width="1918" height="490" alt="image" src="https://github.com/user-attachments/assets/cbd956ea-ab05-41fb-89e4-c9688d531c21" />

Clicking on Confirm Booking navigates to the My Bookings Page

<img width="1919" height="532" alt="image" src="https://github.com/user-attachments/assets/d07bb136-7eb3-4bb7-bd52-854de8c41b00" />

Again Click on My Bookings link

<img width="1889" height="876" alt="image" src="https://github.com/user-attachments/assets/1eb48c92-d6a1-4986-b9b2-e1a6629301f3" />

select * from room where id in (2,3); # rooms for user "paul@hotel.com"

<img width="935" height="308" alt="image" src="https://github.com/user-attachments/assets/bdd64a17-0514-4452-8b96-c484629f6d14" />

Click on Cancel Booking

<img width="1595" height="612" alt="image" src="https://github.com/user-attachments/assets/356ee381-65d4-4588-bf5b-01466272dc4b" />

Click on Ok button

<img width="1818" height="677" alt="image" src="https://github.com/user-attachments/assets/33259388-07a4-40e5-803e-7d97cbc27a5b" />


<img width="1823" height="548" alt="image" src="https://github.com/user-attachments/assets/e57e0520-0f70-462e-aac9-9adff912a127" />


Click on My Bookings

<img width="1896" height="582" alt="image" src="https://github.com/user-attachments/assets/2747a956-85f9-47b4-8ee6-c2564b2a432e" />

**Classes Responsibilties**

   __init__.py -> creates a SQLAlchemy object, Flask app instance, loads the environment variables, Gets the database connection from .env files, loads the SQLALCHEMY_DATABASE_URI,initialize tables,register blueprints, creates database tables .
  __models.py__   -> Create models for 
                      . User table,fields and bookings variable has relationship with Booking table(backref="user") this line is to have back and forth relationship(bidirectional relationship:) ex: user ->                               booking and booking -> user. One user can have many bookings. 
                      . Hotel table,fields and rooms variable has relationship with rooms table(backref="hotel") this line is to have back and forth relationship(bidirectional relationship:) ex: Hotel -> room                            and room to hotel -> One Hotel can have many rooms.
                      . Room table, fields,hotel_id foreign key linked to Hotel table  and  bookings variable has relationship with Room table(backref="room") this line is to have back and forth                                          relationship((bidirectional relationship:) ex: Room -> booking and booking -> Room.  
                      . Booking table fields,user_id foreign key linked to User table column id , room_id foreign key linked to Room table column id
                      
## Future Enhancements

* Admin dashboard for hotel management
* Payment gateway integration
* Booking cancellation & refunds
* Email notifications
* Role-based access control








