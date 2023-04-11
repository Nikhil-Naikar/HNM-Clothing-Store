from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateTimeField, SelectField, SelectMultipleField, \
    IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, URL
import datetime


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    phone_number = StringField("Phone Number")
    type = SelectField(label="User Type", choices=['Owner', 'Customer'], validators=[DataRequired()])
    card_number = StringField("Card Number", validators=[DataRequired()])
    expiry_date = StringField("Expiry Date", validators=[DataRequired()])
    cvv = StringField("CVV", validators=[DataRequired()])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class ItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    img_url = StringField(label="Image Link", validators=[DataRequired(), URL()])
    price = StringField("Price", default="0.00", validators=[DataRequired()])
    sex = SelectField(label="Sex", choices=['Unisex', 'Male', 'Female'], validators=[DataRequired()])
    size = SelectField(label="Size", choices=['Small', 'Medium', 'Large'], validators=[DataRequired()])
    brand = StringField("Brand")
    type = SelectField(label="Type", choices=['Tops', 'Bottoms', 'Accessories', 'Footwear'], validators=[DataRequired()])
    weight = StringField("Weight")
    color = StringField("Color")
    submit = SubmitField("Submit")


class OwnerItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    img_url = StringField(label="Image Link", validators=[DataRequired(), URL()])
    price = StringField("Price", default="0.00", validators=[DataRequired()])
    sex = SelectField(label="Sex", choices=['Unisex', 'Male', 'Female'], validators=[DataRequired()])
    size = SelectField(label="Size", choices=['Small', 'Medium', 'Large'], validators=[DataRequired()])
    brand = StringField("Brand")
    type = SelectField(label="Type", choices=['Tops', 'Bottoms', 'Accessories', 'Footwear'], validators=[DataRequired()])
    color = StringField("Color")
    amount = IntegerField("Amount", validators=[DataRequired()])
    submit = SubmitField("Submit")

class CustomerItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], render_kw={'readonly': True})
    price = StringField("Price", default="0.00", validators=[DataRequired()], render_kw={'readonly': True})
    sex = StringField(label="Sex", validators=[DataRequired()], render_kw={'readonly': True})
    size = SelectField(label="Size", choices=['Small', 'Medium', 'Large'], validators=[DataRequired()])
    brand = StringField("Brand", render_kw={'readonly': True})
    type = StringField(label="Type", validators=[DataRequired()], render_kw={'readonly': True})
    color = StringField("Color", render_kw={'readonly': True})
    amount = IntegerField("Amount")
    submit = SubmitField("Submit")


class BillingForm(FlaskForm):
    card_number = StringField("Card Number", validators=[DataRequired()])
    expiry_date = StringField("Expiry Date", validators=[DataRequired()])
    cvv = StringField("CVV", validators=[DataRequired()])
    submit = SubmitField("Submit")


class OrderForm(FlaskForm):
    total_price = StringField("Total Price ($)", validators=[DataRequired()], render_kw={'readonly': True})
    submit = SubmitField("Submit")
