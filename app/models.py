from . import db
from werkzeug.security import generate_password_hash

class CustomerAccount(db.Model):
    __tablename__ = 'Customer_Accounts'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(255), unique = True)
    password = db.Column(db.String(400))
    name = ""

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = generate_password_hash(password, method = 'pbkdf2:sha256')
        self.name = firstname + lastname

    def is_unique(self, email):
        user = users.query.filter(users.email==email).first()
        if user != None: # the query has returned a user
            flash("Please use a different email.")
            return render_template("newAccount.html")

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_name(self):
        return self.name

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.name)


class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.Integer)
    eventType = db.Column(db.String(80))
    session = db.Column(db.String(80))
    eventStatus = db.Column(db.String(80))
    eventDate = db.Column(db.String(80))
    eventTime = db.Column(db.String(80))
    expectGuestCount = db.Column(db.Integer)
    tableCount = db.Column(db.Integer)
    specialRequests = db.Column(db.String(80))
    phonenumber = db.Column(db.String(80))


    def __init__(self, eventType, session, eventDate, eventTime, expectGuestCount, tableCount, specialRequests, phonenumber, customerid):
        self.customerid = customerid
        self.eventType = eventType
        self.session = session
        self.eventStatus = "pending"
        self.eventDate = str(eventDate)
        self.eventTime = str(eventTime)
        self.expectGuestCount = int(expectGuestCount)
        self.tableCount = int(tableCount)
        self.specialRequests = specialRequests
        self.phonenumber = phonenumber
