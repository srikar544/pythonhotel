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



## Future Enhancements

* Admin dashboard for hotel management
* Payment gateway integration
* Booking cancellation & refunds
* Email notifications
* Role-based access control

