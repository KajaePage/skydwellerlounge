from . import db
from werkzeug.security import generate_password_hash
import psycopg2


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
    eventtype = db.Column(db.String(80))
    session = db.Column(db.String(80))
    eventstatus = db.Column(db.String(80))
    eventdate = db.Column(db.String(80))
    eventtime = db.Column(db.String(80))
    expectguestCount = db.Column(db.Integer)
    tablecount = db.Column(db.Integer)
    specialrequests = db.Column(db.String(1000))
    phonenumber = db.Column(db.String(80))


    def __init__(self, eventType, session, eventDate, eventTime, expectGuestCount, tableCount, specialRequests, phonenumber, customerid):
        self.customerid = customerid
        self.eventtype = eventType
        self.session = session
        self.eventstatus = "pending"
        self.eventdate = str(eventDate)
        self.eventtime = str(eventTime)
        self.expectguestcount = int(expectGuestCount)
        self.tablecount = int(tableCount)
        self.specialrequests = specialRequests
        self.phonenumber = phonenumber

    
    def del_event(id):
        db = psycopg2.connect(host="localhost",database="SDUL Database", user="demitri", password="sky")
        cur = db.cursor()
        cur.execute("DELETE FROM events WHERE id = %s", (id,))
        db.commit()


    
class Menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    itemtype = db.Column(db.String(80))
    itemtitle1 = db.Column(db.String(200))
    itemtitle2 = db.Column(db.String(200))
    itemprice1 = db.Column(db.Integer)
    itemprice2 = db.Column(db.Integer)
    itemdiscription = db.Column(db.String(1000))
    itemadditionaldetails = db.Column(db.String(1000))

    def __init__(self, itemType, itemTitle1, itemTitle2, itemPrice1, itemPrice2, itemDiscription, itemAdditionalDetails):
        self.itemtype = itemType
        self.itemtitle1 = itemTitle1
        self.itemtitle2 = itemTitle2
        self.itemprice1 = itemPrice1
        self.itemprice2 = itemPrice2
        self.itemdiscription = itemDiscription
        self.itemadditionalDetails = itemAdditionalDetails


    def del_item(id):
        db = psycopg2.connect(host="localhost",database="SDUL Database", user="demitri", password="sky")
        cur = db.cursor()
        cur.execute("DELETE FROM menu WHERE id = %s", (id,))
        db.commit()


    def getby_itemType(itemType):
        db = psycopg2.connect(host="localhost",database="SDUL Database", user="demitri", password="sky")
        cur = db.cursor()
        cur.execute("select * from menu where itemtype = %s", (itemType,))
        items = cur.fetchall()
        return items

    def update_Row(itemtype,itemtitle1,itemtitle2,itemprice1,itemprice2,itemdiscription,itemadditionalDetails, id):
        db = psycopg2.connect(host="localhost",database="SDUL Database", user="demitri", password="sky")
        cur = db.cursor()
        cur.execute("UPDATE menu SET itemtype = %s, itemtitle1 = %s, itemtitle2 = %s, itemprice1 = %s, itemprice2 = %s,  itemdiscription = %s, itemadditionalDetails = %s WHERE id = %s", (itemtype,itemtitle1,itemtitle2,itemprice1,itemprice2,itemdiscription,itemadditionalDetails, id))
        updated_rows = cur.rowcount
        db.commit()
        cur.close()
   


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    customerid = db.Column(db.String(80))
    itemid = db.Column(db.String(80))
    itemname = db.Column(db.String(80))
    itemtype = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)


    def __init__(self, customerid, itemid, itemname, itemtype, quantity, price):
        self.customerid = customerid
        self.itemid = itemid
        self.itemname = itemname
        self.itemtype = itemtype
        self.quantity = quantity
        self.price = price

    




