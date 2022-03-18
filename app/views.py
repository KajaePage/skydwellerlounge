"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
cust = 0
###
# Routing for your application.
###

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

            return redirect(url_for('home'))

    return render_template("newAccount.html" , form = form)



@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/menu')
def viewmenu():
    return render_template('menu.html')


from app.forms import BookEventForm
from app.models import Event

@app.route('/bookevent', methods = ['GET', 'POST'])
@login_required
def bookevent():
    form = BookEventForm()

    if request.method == 'POST':
        # if form.validate_on_submit():
        eventType = request.form['eventType']
        session = request.form['session']
        eventDate = request.form['eventDate']
        eventTime = request.form['eventTime']
        expectGuestCount = request.form['expectGuestCount']
        tableCount = request.form['tableCount']
        specialRequests = request.form['specialRequests']
        phonenumber = request.form['phonenumber']

        print(cust)
        event = Event(eventType, session, eventDate, eventTime, expectGuestCount, tableCount, specialRequests, phonenumber, cust)
        db.session.add(event)
        db.session.commit()

        return redirect(url_for('profile'))

    return render_template('bookevent.html', form = form)

@app.route('/adminSystem')
def admin():
    return render_template('managementSidebar.html')


def get_customer_info(customer):
    customerinfo = [customer]

    return customerinfo

@app.route('/myprofile')
@login_required
def profile():
    return render_template('profile.html', customerinfo = get_customer_info(cust))


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
                return redirect(url_for("profile"))

    return render_template('login.html', form = form)


@app.route("/logout")
def logout():
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
