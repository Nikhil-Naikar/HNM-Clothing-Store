from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateTimeField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Email, EqualTo, URL
import datetime


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    phone_number = StringField("Phone Number")
    type = SelectField(label="User Type", choices=['Owner', 'Customer'], validators=[DataRequired()])
    address = StringField("Address")
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
    # type = StringField(label="Type (eg. Tops, Bottoms, Accessories, Footwear)", validators=[DataRequired()])
    type = SelectField(label="Type", choices=['Tops', 'Bottoms', 'Accessories', 'Footwear'], validators=[DataRequired()])
    weight = StringField("Weight")
    # colors = SelectMultipleField(label="Colors", choices=['Black', 'White', 'Brown', 'Grey', 'Blue', 'Red',
    #                                                       'Green', 'Pink', 'Purple', 'Yellow', 'Orange'])
    color = StringField("Color")
    submit = SubmitField("Submit")


class ItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    img_url = StringField(label="Image Link", validators=[DataRequired(), URL()])
    price = StringField("Price", default="0.00", validators=[DataRequired()])
    sex = SelectField(label="Sex", choices=['Unisex', 'Male', 'Female'], validators=[DataRequired()])
    size = SelectField(label="Size", choices=['Small', 'Medium', 'Large'], validators=[DataRequired()])
    brand = StringField("Brand")
    # type = StringField(label="Type (eg. Tops, Bottoms, Accessories, Footwear)", validators=[DataRequired()])
    type = SelectField(label="Type", choices=['Tops', 'Bottoms', 'Accessories', 'Footwear'], validators=[DataRequired()])
    weight = StringField("Weight")
    # colors = SelectMultipleField(label="Colors", choices=['Black', 'White', 'Brown', 'Grey', 'Blue', 'Red',
    #                                                       'Green', 'Pink', 'Purple', 'Yellow', 'Orange'])
    color = StringField("Color")
    submit = SubmitField("Submit")

class ItemForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    img_url = StringField(label="Image Link", validators=[DataRequired(), URL()])
    price = StringField("Price", default="0.00", validators=[DataRequired()])
    sex = SelectField(label="Sex", choices=['Unisex', 'Male', 'Female'], validators=[DataRequired()])
    size = SelectField(label="Size", choices=['Small', 'Medium', 'Large'], validators=[DataRequired()])
    brand = StringField("Brand")
    # type = StringField(label="Type (eg. Tops, Bottoms, Accessories, Footwear)", validators=[DataRequired()])
    type = SelectField(label="Type", choices=['Tops', 'Bottoms', 'Accessories', 'Footwear'], validators=[DataRequired()])
    weight = StringField("Weight")
    # colors = SelectMultipleField(label="Colors", choices=['Black', 'White', 'Brown', 'Grey', 'Blue', 'Red',
    #                                                       'Green', 'Pink', 'Purple', 'Yellow', 'Orange'])
    color = StringField("Color")
    submit = SubmitField("Submit")


class BillingForm(FlaskForm):
    card_number = StringField("Card Number", validators=[DataRequired()])
    expiry_date = StringField("Expiry Date", validators=[DataRequired()])
    cvv = StringField("CVV", validators=[DataRequired()])
    submit = SubmitField("Submit")


class OrderForm(FlaskForm):
    total_price = StringField("Total Price ($)", validators=[DataRequired()], render_kw={'readonly': True})
    submit = SubmitField("Submit")
