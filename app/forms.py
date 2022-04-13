from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, DateField, PasswordField, EmailField, IntegerField, TextAreaField, SelectField, DecimalField
from wtforms.validators import DataRequired, InputRequired
from wtforms.validators import ValidationError
from app.models import CustomerAccount
from flask import flash

def validate_email(self, field):
    if CustomerAccount.get_email(field.data)==field.data:
        flash('Email Already Exists.')
        raise ValidationError('Email Already Exists.')
            

class newAccountForm(FlaskForm):
    firstname = StringField("Firstname", validators = [DataRequired()])
    lastname = StringField("Lastname", validators = [DataRequired()])
    email = EmailField("Email", validators = [InputRequired(),validate_email])
    password = PasswordField("Password", validators = [InputRequired()])

    

class Delete(FlaskForm):
    delete = IntegerField("", validators=[DataRequired()])

class UpdateStatus(FlaskForm):
    updateid = IntegerField("", validators=[DataRequired()])
    status = SelectField('Change Status:', choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('denied', 'Denied')], validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class BookReservationsForm(FlaskForm):
    reservationsType = SelectField('', choices=[('null', 'Select Type of Event'), ('birthday', 'Birthday'), ('anniversary', 'Anniversary'), ('date', 'Date')], validators=[DataRequired()])
    session = SelectField('', choices=[('null', 'Your Session'), ('brunch', 'Brunch'), ('dinner', 'Dinner'), ('lunch', 'Lunch')], validators=[DataRequired()])
    reservationsDate = DateField('', format='%m/%d/%Y', validators = [DataRequired()])
    reservationsTime = RadioField('', choices = [('12:00','12:00'),('12:15','12:15'),('12:30','12:30')], validators = [DataRequired()])
    expectGuestCount = IntegerField("", validators=[DataRequired()])
    tableCount = IntegerField("", validators=[DataRequired()])
    specialRequests = TextAreaField("", validators=[DataRequired()])
    phonenumber = StringField("", validators=[DataRequired()])


class AddDrinkMenuItem(FlaskForm):
    itemType = SelectField('Item Type', choices=[(' ', 'Show Options'), ('cocktail', 'Cocktail'), ('mixer', 'Mixer'), ('red-wine', 'Red Wine'), ('white-wine', 'White Wine'), ('sparkling', 'Sparkling'), ('beers', 'Beers'), ('whiskey', 'Whiskey/Scotch')], validators=[DataRequired()])
    itemTitle1 = StringField("Item Name", validators=[DataRequired()])
    itemTitle2 = StringField("Second Option")
    itemPrice1 = IntegerField("Item Price",  validators=[DataRequired()])
    itemPrice2 = IntegerField("Second Price")
    itemDiscription = TextAreaField("Item Discription")
    itemAdditionalDetails = TextAreaField("Item Substitutes")


