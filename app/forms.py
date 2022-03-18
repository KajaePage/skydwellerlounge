from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, DateField, PasswordField, EmailField, IntegerField, TextAreaField, SelectField
from wtforms.validators import DataRequired, InputRequired

class newAccountForm(FlaskForm):
    firstname = StringField("Firstname", validators = [DataRequired()])
    lastname = StringField("Lastname", validators = [DataRequired()])
    email = EmailField("Email", validators = [InputRequired()])
    password = PasswordField("Password", validators = [InputRequired()])


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