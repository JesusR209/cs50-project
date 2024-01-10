


CS50 Project: Appointment Booking App
This is a simple appointment booking app built using Python 3, Flask, Jinja2, and SQL.

Features
User-friendly Interface: Easy-to-use web interface for booking appointments.
Date and Time Selection: Users can choose their preferred date and time for appointments.
SQL Database: Appointments are stored in an SQL database for persistence.
Prerequisites
Make sure you have the following installed:

Python 3
pip
Flask
Jinja2
SQL Database (Specify the database you're using)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/cs50-project.git
cd cs50-project
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
python app.py
Visit http://localhost:5000 in your browser.

Usage
Navigate to the homepage.
Choose the date and time for your appointment.
Enter your name and any additional information.
Click on the "Book Appointment" button.
View booked appointments on the registrants page.
Database Configuration
Configure your SQL database connection in the config.py file.

python
Copy code
# config.py

SQLALCHEMY_DATABASE_URI = 'your_database_uri'
SQLALCHEMY_TRACK_MODIFICATIONS = False
