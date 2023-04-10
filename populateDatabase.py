from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from main2 import User



# Load .env file with the SECRET_KEY
load_dotenv("./.env")

# Create Flask application instance
app = Flask(__name__)
# Create a database file called clothing.db or connect to it, if it already exists
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
# Set to False disables tracking modifications of objects and uses less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Secret key allows Flask-Login to use sessions (allows one to store info specific to a
# user from one request to another) for authentication

app.config['SECRET_KEY'] = os.urandom(32)
# Packages Bootstrap CSS extension into the app
Bootstrap(app)
# SQLAlchemy
db = SQLAlchemy(app)
# LoginManager contains the code that lets your application and Flask - Login work together, such as how to
# load a user from an ID, where to send users when they need to log in, etc
login_manager = LoginManager()
# Configure actual application object for login
login_manager.init_app(app)

Bob = User()
Bob.username = "Bob"
Bob.email_address = "bob@email.com"
Bob.password = generate_password_hash("bob", method="pbkdf2:sha256", salt_length=8)
Bob.phone_number = "587-111-2323"
Bob.type = "Customer"
Bob.shipping_provider_id = 000

db.session.add(Bob)
db.session.commit()
