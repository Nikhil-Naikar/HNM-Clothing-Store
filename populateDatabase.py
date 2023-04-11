

from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column, composite, with_polymorphic
from flask_login import LoginManager, UserMixin, current_user, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os
from functools import wraps
# from main2 import User, ShippingProvider, Warehouse, Inventory, Billing, Item, Order, PlacedIn



# Load .env file with the SECRET_KEY
load_dotenv("./.env")

# Create Flask application instance
app = Flask(__name__)
# Create a database file called clothing.db or connect to it, if it already exists
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///demoDatabase.db"
# Set to False disables tracking modifications of objects and uses less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Secret key allows Flask-Login to use sessions (allows one to store info specific to a
# user from one request to another) for authentication
# app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
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


# User Database Table
class User(UserMixin, db.Model):
    __tablename__ = "user"  # Table name
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email_address = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
    phone_number = db.Column(db.String(15))
    type = db.Column(db.String(8), nullable=False)
    shipping_provider_id = db.Column(db.Integer, db.ForeignKey("shipping_provider.id"))

    # Establish one-to-many relationship
    warehouse = relationship("Warehouse", back_populates="user")

    # Establish one-to-many relationship from Owner to Item
    item = relationship("Item", back_populates="user")

    # Establish one-to-one relationship from Owner to Inventory
    # relationship.uselist flag indicates the placement of a scalar attribute instead of a collection on the “many”
    # side of the relationship.
    inventory = relationship("Inventory", uselist=False, back_populates="user")

    # Establish one-to-one relationship from Customer to Billing
    billing = relationship("Billing", uselist=False, back_populates="user")

    # Establish one-to-one relationship from Customer to Order
    order = relationship("Order", uselist=False, back_populates="user")

    # Establish many-to-one relationship from Customer to ShippingProvider
    shipping_provider = relationship("ShippingProvider", back_populates="user")

class Warehouse(db.Model):
    __tablename__ = "warehouse"  # Table name
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    location = db.Column(db.String(25), nullable=False)
    # Establish one-to-many relationship from Owner to Warehouse - creating a foreign key on the 'many' table warehouse,
    # that references the 'one' owner
    # foreign key is placed under the new field owner_id
    # "owner.id" The owner refers to the tablename of the Owner class.
    buyer_id = db.Column(db.Integer, db.ForeignKey("user.id"))  # adds new column in Warehouse for foreign key
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))

    user = relationship("User", back_populates="warehouse")
    # Establish many-to-one relationship from Warehouse to Inventory
    inventory = relationship("Inventory", back_populates="warehouses")

class Inventory(db.Model):
    __tablename__ = "inventory"  # Table name
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    stock = db.Column(db.Integer, nullable=False)
    last_updated = db.Column(db.String(25), nullable=False)
    updater_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Establish many-to-one relationship from Warehouse to Inventory
    warehouses = relationship("Warehouse", back_populates="inventory")

    # Establish one-to-one relationship from Owner to Inventory
    user = relationship("User", back_populates="inventory")

    # Establish one-to-many relationship from Inventory to Item
    item = relationship("Item", back_populates="inventory")

class PlacedIn(db.Model):
    __tablename__ = "placed_in"
    # Fields
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), primary_key=True)
    order_num = db.Column(db.Integer, db.ForeignKey('order.order_num'), primary_key=True)
    amount = db.Column(db.Integer, nullable=False)

    # Establishing many to many relationship
    customerOrder = relationship("Order", back_populates="items")
    customerItem = relationship("Item", back_populates="customerOrders")

class Order(db.Model):
    __tablename__ = "order"  # Table name
    # Fields
    order_num = db.Column(db.Integer, nullable=False, primary_key=True)
    order_date = db.Column(db.String(25))
    total_price = db.Column(db.Float(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    shipping_provider_id = db.Column(db.Integer, db.ForeignKey('shipping_provider.id'))

    # Establish one-to-one relationship from Customer to Order
    user = relationship("User", back_populates="order")

    # Establish many-to-one relationship from Order to ShippingProvider
    shipping_provider = relationship("ShippingProvider", back_populates="orders")

    # Establish many-to-many relationship
    items = relationship('PlacedIn', back_populates="customerOrder")

class Item(db.Model):
    __tablename__ = "item"  # Field name
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    img_url = db.Column(db.String, nullable=False)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.Float(10), nullable=False)
    sex = db.Column(db.String(6))
    size = db.Column(db.String(6))
    brand = db.Column(db.String(25))
    type = db.Column(db.String(11))
    color = db.Column(db.String(25))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'))

    # Establish one-to-many relationship from Owner to Item
    user = relationship("User", back_populates="item")

    # Establish one-to-many relationship from Inventory to Item
    inventory = relationship("Inventory", back_populates="item")

    # Establish many-to-many relationship
    customerOrders = relationship('PlacedIn', back_populates="customerItem")

class Billing(db.Model):
    __tablename__ = "billing"  # Table name
    # Fields
    card_number = db.Column(db.String(20), primary_key=True)
    expiry_date = db.Column(db.String(10))
    cvv = db.Column(db.String(3))

    # Establish one-to-one relationship from Customer to Billing
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User", back_populates="billing")


class ShippingProvider(db.Model):
    __tablename__ = "shipping_provider"  # Table name
    # Fields
    id = db.Column(db.Integer, primary_key=True)
    travel = db.Column(db.String(10), nullable=False) # ship/train/truck/airplane
    weight = db.Column(db.Float, nullable=False)

    # Establish many-to-one relationship from Customer to ShippingProvider
    user = relationship("User", back_populates="shipping_provider")

    # Establish many-to-one relationship from Order to ShippingProvider
    orders = relationship("Order", back_populates="shipping_provider")



def new_user(username,email_address,password,phone_number,type,shipping_provider):
    temp = User()
    temp.username = username
    temp.email_address = email_address
    temp.password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
    temp.phone_number = phone_number
    temp.type = type
    temp.shipping_provider_id = shipping_provider
    db.session.add(temp)
    db.session.commit()

def new_shipping_provider(id, travel, weight):
    temp = ShippingProvider()
    temp.id = id
    temp.travel = travel
    temp.weight = weight
    db.session.add(temp)
    db.session.commit()

def new_warehouse(id, name, location, buyer_id, inventory_id):
    temp = Warehouse()
    temp.id = id
    temp.name = name
    temp.location = location
    temp.buyer_id = buyer_id
    temp.inventory_id = inventory_id
    db.session.add(temp)
    db.session.commit()

def new_inventory(id, stock, last_updated, updater_id):
    temp = Inventory()
    temp.id = id
    temp.stock = stock
    temp.last_updated = last_updated
    temp.updater_id = updater_id
    db.session.add(temp)
    db.session.commit()

def new_billing(card_number, expiry_date, cvv, user_id):
    temp = Billing()
    temp.card_number = card_number
    temp.expiry_date = expiry_date
    temp.cvv = cvv
    temp.user_id = user_id
    db.session.add(temp)
    db.session.commit()


def new_item(id, img_url, name, price, sex, size, brand, type, color, user_id, inventory_id):
    temp = Item()
    temp.id = id
    temp.img_url = img_url
    temp.name = name
    temp.price = price
    temp.sex = sex
    temp.size = size
    temp.brand = brand
    temp.type = type
    temp.color = color
    temp.user_id = user_id
    temp.inventory_id = inventory_id
    db.session.add(temp)
    db.session.commit()

def new_order(order_num, order_date, total_price, user_id, ship_id):
    temp = Order()
    temp.order_num = order_num
    temp.order_date = order_date
    temp.total_price = total_price
    temp.user_id = user_id
    temp.shipping_provider_id = ship_id
    db.session.add(temp)
    db.session.commit()

def new_placed_in(item_id, order_num, amount):
    temp = PlacedIn()
    temp.item_id = item_id
    temp.order_num = order_num
    temp.amount = amount
    db.session.add(temp)
    db.session.commit()

with app.app_context():
    db.create_all()  # Create database
    new_user("admin", "admin@email.com", "admin", "587-344-1212", "Owner", 111)
    new_user("c1", "c1@email.com", "c1", "587-554-1232", "Customer", 111)
    new_user("c2", "c2@email.com", "c2", "587-366-1679", "Customer", 111)
    new_shipping_provider(111, "ship", 50.00)
    new_inventory(456, 100, "07/04/2023 19:06:28", 1)
    new_inventory(345, 100, "07/04/2023 20:11:12", 1)
    new_inventory(234, 100, "03/04/2023 13:54:02", 1)
    new_inventory(555, 100, "02/04/2023 14:23:05", 1)
    new_inventory(879, 100, "05/04/2023 09:04:50", 1)
    new_inventory(324, 100, "11/04/2023 04:16:43", 1)
    new_warehouse(246, "Bob's Goods", "vancouver", 1, 456)
    new_billing("1234234513241345", "03/12", "132", 2)
    new_billing("9343132546532435", "05/06", "890", 3)
    new_item(1, "https://image.uniqlo.com/UQ/ST3/ca/imagesgoods/462439/item/cagoods_31_462439.jpg?width=750", "ATTACK ON TITAN SHORT SLEEVE UT", 20.0, "Male", "Medium", "Uniqlo", "Tops", "Brown", 1, 456)
    new_item(2, "https://image.uniqlo.com/UQ/ST3/ca/imagesgoods/455359/item/cagoods_23_455359.jpg?width=750", "UNIQLO U AIRISM COTTON CREW NECK OVERSIZED T-SHIRT", 24.90, "Male", "Large", "Uniqlo", "Tops", "Yellow", 1, 345)
    new_item(3, "https://image.uniqlo.com/UQ/ST3/WesternCommon/imagesgoods/444527/item/goods_72_444527.jpg?width=750", "SUPIMA COTTON CREW NECK SHORT SLEEVE T-SHIRT", 12.90, "Female", "Small", "Uniqlo", "Tops", "Purple", 1, 234)
    new_item(4, "https://image.uniqlo.com/UQ/ST3/ca/imagesgoods/456116/item/cagoods_06_456116.jpg?width=750", "PLEATED WIDE PANTS", 40.0, "Female", "Small", "Uniqlo", "Bottoms", "Grey", 1, 555)
    new_item(5, "https://image.uniqlo.com/UQ/ST3/WesternCommon/imagesgoods/458268/item/goods_24_458268.jpg?width=750", "UV PROTECTION PILE BUCKET HAT", 15.0, "Unisex", "Small", "Uniqlo", "Accessories", "Orange", 1, 879)
    new_item(6, "https://nb.scene7.com/is/image/NB/m990bk6_nb_05_i?$pdpflexf22x$&qlt=80&fmt=webp&wid=880&hei=880", "USA 990v6", 260.0, "Unisex", "Medium", "New Balance", "Footwear", "Black", 1, 324)
    new_order(11, "12/04/2023 14:06:48", 260.0, 2, 111)
    new_order(22, "22/04/2023 11:36:24", 35.0, 3, 111)
    new_placed_in(6, 11, 1)
    new_placed_in(1, 22, 1)
    new_placed_in(5, 22, 1)
