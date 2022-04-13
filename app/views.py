"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash, send_from_directory, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash


from app.forms import AddDrinkMenuItem
from app.forms import Delete
from app.forms import UpdateStatus
from app.models import Menu

import locale 
from sqlalchemy import or_


cust = 0
###
# Routing for your application.
###

import psycopg2

# db = psycopg2.connect(host="localhost",database="SDUL Database", user="demitri", password="sky")
# cur = db.cursor()
# cur.execute("DELETE FROM cart WHERE id = %s", (0,))
# print('should delte')
# db.commit()

# Menu.update_Row("cocktail","Lemonade Frozen"," ",500,1,"Syrup mixed with lime juice and garnished with lemon wheel."," ", 1)



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")




from app.forms import newAccountForm
from app.models import CustomerAccount

@app.route('/createaccount', methods = ['GET', 'POST'])
def createAccount():

    form = newAccountForm()

    if request.method == "POST":
        if form.validate_on_submit():
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            password = form.password.data

            customer = CustomerAccount(firstname, lastname, email, password)
            db.session.add(customer)
            db.session.commit()

            login_user(customer)
            name = customer.firstname + customer.lastname 

            global cust 
            cust = customer.id
            return redirect(url_for("myprofile"))

    return render_template("newAccount.html" , form = form)



@app.route('/contact')
def contact():
    return render_template('contact.html')



from app.models import Cart

@app.route('/process', methods=['GET','POST'])
def processCart():

    recieved = False
    if request.method == 'POST':
        cart = request.get_json(force=True)
        
        if cart:
            
            if Cart.is_present(cust):
                Cart.remove(cust)
                addCart = Cart(customerid= cust, cartinfo={'cart':cart})
                db.session.add(addCart)
                db.session.commit()

            else:
                addCart = Cart(customerid= cust, cartinfo={'cart':cart})
                db.session.add(addCart)
                db.session.commit()

            return jsonify({'message': "Data recieved"})
        
        else:
            return jsonify({'error' : 'Data missing'})

    elif  request.method == 'GET':
        return jsonify({'message': 'hello'})


from app.models import Order

@app.route('/placedorder', methods=['POST', 'GET'])
@login_required
def placeorder():
    if request.method=='POST':
        print('Post processed successfully...')
        placeorder = request.get_json(force=True)
        print(placeorder)
        
        if placeorder:
            print("place order")
            addOrder = Order(customerid= cust, orderdetails={'cart':placeorder},status='pending')
            db.session.add(addOrder)
            db.session.commit()
            return redirect(url_for("myprofile"))

        else:
            return jsonify({'message': "Data error"})
    return redirect(url_for("login"))
            


@app.route('/drinksmenu', methods=['GET','POST'])
def viewmenu():

    cocktailItems = Menu.getby_itemType("cocktail")   
    mixerItems = Menu.getby_itemType("mixer")
    redwineItems = Menu.getby_itemType("red-wine") 
    whitewineItems = Menu.getby_itemType("white-wine") 

    

    return render_template('drinksmenu.html', cocktailItems= cocktailItems, mixerItems=mixerItems, redwineItems=redwineItems, whitewineItems=whitewineItems)


from app.forms import BookReservationsForm
from app.models import Reservations

@app.route('/make/reservations', methods = ['GET', 'POST'])
@login_required
def makereservations():
    form = BookReservationsForm()

    if request.method == 'POST':
        # if form.validate_on_submit():
        reservationsType = str(request.form['reservationsType'])
        session = str(request.form['session'])
        reservationsDate = str(request.form['reservationsDate'])
        reservationsTime = str(request.form['reservationsTime'])
        expectGuestCount = str(request.form['expectGuestCount'])
        tableCount = str(request.form['tableCount'])
        specialRequests = str(request.form['specialRequests'])
        phonenumber = str(request.form['phonenumber'])

        print(reservationsType, session, reservationsDate, reservationsTime, expectGuestCount, tableCount, specialRequests, phonenumber, cust)
        reservations = Reservations(reservationsType, session, reservationsDate, reservationsTime, expectGuestCount, tableCount, specialRequests, phonenumber, cust)
        db.session.add(reservations)
        db.session.commit()

        return redirect(url_for('myprofile'))

    return render_template('makereservations.html', form = form)


@app.route('/book/event', methods = ['GET', 'POST'])
@login_required
def bookevent():
    return render_template('eventCalender.html')



def get_customer_info(customer):
    customerinfo = [customer]

    return customerinfo

@app.route('/myprofile', methods = ['GET', 'POST'])
@login_required
def myprofile():

    return render_template('myprofile.html', customerinfo = get_customer_info(cust))



###
# The functions below should be applicable to all Flask apps.
###


from app.forms import LoginForm
@app.route('/login', methods= ['GET','POST'])
def login():

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            customer = CustomerAccount.query.filter_by(email=email).first()

            if customer is not None and check_password_hash(customer.password, password):
                login_user(customer)
                name = customer.firstname + customer.lastname 

                global cust 
                
                cust = customer.id

                print(cust)
                return redirect(url_for("myprofile"))

    return render_template('login.html', form = form)


# Management View Routes
@app.route("/reservations", methods=['GET','POST'])
def mreservations():

    update = UpdateStatus()
    delete = Delete()
    from datetime import datetime
    today = datetime.today().strftime('%Y-%m-%d')
    reservations = Reservations.get_reservations(today)

    if request.method == 'POST':
        if delete.validate_on_submit():
            id = request.form['delete']
            Reservations.del_item(id)
            return redirect(url_for("mreservations"))

        if update.validate_on_submit():
            updateid = request.form['updateid']
            status = request.form['status']
            Reservations.update_status(status,updateid)
            return redirect(url_for("mreservations"))

    return render_template('mreservations.html', reservations=reservations, update = update, delete =delete)


@app.route("/dashboard")
def mdashboard():
    reservations = db.session.query(Reservations).all()

    return render_template('mdashboard.html', reservations=reservations, active='active')


@app.route("/notifications")
def mnotifications():
    reservations = db.session.query(Reservations).all()
    return render_template('mnotifications.html', reservations=reservations, active='active')


@app.route("/manageorders")
def morders():
    
    return render_template('morders.html', active='active')

@app.route("/events")
def mevents():
    # events = db.session.query(Event).all()
    return render_template('mevents.html') #, events=events, active='active')



@app.route("/managemenu", methods=['GET','POST'])
def mmenu():

    form = AddDrinkMenuItem()
    update = AddDrinkMenuItem()
    delete = Delete()

    cocktailItems = Menu.getby_itemType("cocktail")
    cocktailItems = Menu.getby_itemType("cocktail")   
    mixerItems = Menu.getby_itemType("mixer")
    redwineItems = Menu.getby_itemType("red-wine") 
    whitewineItems = Menu.getby_itemType("white-wine") 
    wineItems = redwineItems + whitewineItems
    
    if request.method == 'POST':
        
        if form.validate_on_submit():
            itemType = request.form['itemType']
            itemTitle1 = request.form['itemTitle1']
            itemTitle2 = " "
            itemPrice1 = request.form['itemPrice1']
            itemPrice2 = request.form['itemPrice2']

            itemDiscription = request.form['itemDiscription']
            itemAdditionalDetails = request.form['itemAdditionalDetails']


            menuItem = Menu(itemType, itemTitle1, itemTitle2, itemPrice1, itemPrice2, itemDiscription, itemAdditionalDetails)
            db.session.add(menuItem)
            db.session.commit()

            return redirect(url_for("mmenu"))

        
        
        if delete.validate_on_submit():
            id = request.form['delete']
            Menu.del_item(id)
            return redirect(url_for("mmenu"))

    return render_template('mmenu.html', form=form, cocktailItems = cocktailItems, mixerItems=mixerItems, wineItems=wineItems, active='active', delete=delete)

@app.route("/customers")
def mcustomers():
    customers = db.session.query(CustomerAccount).all()
    return render_template('mcustomers.html', customers=customers, active='6')


@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)






@app.route("/update", methods=['GET','POST'])
def logout():
    # cart = AddToCart()

    # if request.method == 'POST':
    #     if cart.validate_on_submit():
    #         cartInfo = request.form['cartInfo']

    #         addCart = Cart(cust, cartInfo)
    #         db.session.add(addCart)
    #         db.session.commit()


    logout_user()
    return redirect(url_for("home"))

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return CustomerAccount.query.get(int(id))





# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
