Python Hotel Booking Platform 📋

This project is a **Hotel Booking System** that allows user to browse available hotels and make bookings based on real time availability . This application is designed in a **Production-Ready architecture**,
will support **multiple concurrent users** and build to be **scalable on AWS**. It follows modular design priniciples to ensure performance,security and future extensibility.

**TechStack used for this project**


| **Layer**      | **Technology**          |
| -------------- | ----------------------- |
| Backend        | Flask                   |
| ORM            | Flask-SQLAlchemy        |
| Database       | MySQL                   |
| Authentication | Flask-Login             |
| Templates      | Jinja2                  |
| Styling        | HTML / CSS (extendable) |

**Application Features**

 * User registration functionality for new users.
 * Secure login for existing users.
 * Hotel booking based on real-time room availability.
 * Prevention of double bookings by restricting reservations when rooms are unavailable, even if multiple users attempt to book the same hotel at the same time.

**Database Schema**


| **Table**      | **Primary Column**      |  ** Foreign Key ** |
| -------------- | ----------------------- |  ----------------  |
|    User        |      id                 |                    |
|   hotel        |      id                 |                    |
|   room         |     id                  |  hotel_id          |
|   booking      |     id                  |  user_id,room_id   |
|                |                         |                    |


 hotel table column id is mapped to User table column id 
 booking hotel table column user_id mapped to user table column id
 room table column id mapped to booking table column room_id

 Example Query: 
 select * from user u inner join booking b on u.id=b.user_id 
  inner join room r on r.id=b.room_id

 <img width="940" height="343" alt="image" src="https://github.com/user-attachments/assets/2e257edb-721f-47e6-aca2-b223917d6235" />
