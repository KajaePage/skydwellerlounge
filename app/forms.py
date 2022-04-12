from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, DateField, PasswordField, EmailField, IntegerField, TextAreaField, SelectField, DecimalField
from wtforms.validators import DataRequired, InputRequired

class newAccountForm(FlaskForm):
    firstname = StringField("Firstname", validators = [DataRequired()])
    lastname = StringField("Lastname", validators = [DataRequired()])
    email = EmailField("Email", validators = [InputRequired()])
    password = PasswordField("Password", validators = [InputRequired()])

class Delete(FlaskForm):
    delete = IntegerField("", validators=[DataRequired()])
    

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class BookEventForm(FlaskForm):
    eventType = SelectField('', choices=[('null', 'Select Type of Event'), ('birthday', 'Birthday'), ('anniversary', 'Anniversary'), ('date', 'Date')], validators=[DataRequired()])
    session = SelectField('', choices=[('null', 'Your Session'), ('brunch', 'Brunch'), ('dinner', 'Dinner'), ('lunch', 'Lunch')], validators=[DataRequired()])
    eventDate = DateField('', format='%m/%d/%Y', validators = [DataRequired()])
    eventTime = RadioField('', choices = [('12:00','12:00'),('12:15','12:15'),('12:30','12:30')], validators = [DataRequired()])
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


# class Cart(FlaskForm):
