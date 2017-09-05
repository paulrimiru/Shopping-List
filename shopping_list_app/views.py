"""
Class for rendering my views in template folder
"""
from functools import wraps
from flask import session, render_template, redirect, url_for, request

from shopping_list_app import APP
from shopping_list_app.user import User
from shopping_list_app.admin import Admin
from shopping_list_app.shoppinglist import ShoppingList
from shopping_list_app.item import Item

ADMIN = Admin()
USER = User()


def authorisation(func):
    """Wrapper to check user authorization"""
    @wraps(func)
    def auth(*args, **kargs):
        """checks for if the user is logged in through the session"""
        if session.get('signed_in'):
            return func(*args, **kargs)
        else:
            return redirect(url_for('login'))
    return auth
@APP.route('/')
@APP.route('/index')
def index():
    """
    Render the index page
    """
    return render_template("index.html")

@APP.route('/dashboard/')
@authorisation
def dashboard():
    """
    Render the user dashboard
    """
    return render_template("dashboard.html")

@APP.route('/login/')
def login():
    """
    Render login page used to sign in
    """
    return render_template("login.html")

@APP.route('/register/')
def register():
    """
    Render Register page used to sign up the user
    """
    return render_template("register.html")

@APP.route('/create_shoppinglist/')
@authorisation
def create_shoppinglist():
    """
    Render view for creating new shopping lists
    """
    return render_template("create_shoppinglist.html")

@APP.route('/edit_shoppinglist/')
@authorisation
def edit_shoppinglist():
    """
    Render view for editing shopping lists
    """
    return render_template("edit_shoppinglist.html")
@APP.errorhandler(404)
def page_not_found_error(error):
    """Renders page if request is not found"""
    return render_template("404.html"), 404
@APP.errorhandler(500)
def internal_server_error(error):
    """Renders page if there is internal service error"""
    return render_template("500.html"), 500
@APP.route('/create_user', methods=['POST', 'GET'])
def create_user():
    """Method retrieves data from post request and creates a user"""
    if request.method == 'POST':
        fname = request.form['firstname']
        sname = request.form['secondname']
        email = request.form['email']
        password = request.form['password']

        USER.instastiate_user(fname, sname, email, password)

        ADMIN.add_user(USER)

        return redirect(url_for('login'))
@APP.route('/authenticate', methods=['POST', 'GET'])
def authenticate():
    """Authenticates the user before login"""
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        status = ADMIN.check_password(email, password)
        if status['success']:
            session['email'] = email
            session['signed_in'] = True
            return render_template("dashboard.html", username=status['username'])
        else:
            if status.get('has_account'):
                return status["message"]
            else:
                return redirect(url_for('register'))
@APP.route('/createlist', methods=['POST', 'GET'])
@authorisation
def createlist():
    """creates a list for a user"""
    retrieved_shoppinglist = []
    if request.method == 'POST':
        lname = request.passform['listname']
        ldesc = request.form['description']
        shoppinglistobject = ShoppingList(lname, ldesc)
        USER.create_list(shoppinglistobject)
        retrieved_shoppinglist = USER.get_all()
        
        print (retrieved_shoppinglist)
    return render_template("dashboard.html", user_shoppinglists=retrieved_shoppinglist,
                           username=USER.username)
@APP.route('/remove_lists', methods=['POST', 'GET'])
@authorisation
def remove_list():
    """Removes lists from users"""
    if request.method == 'POST':
        name = request.form['name']
        USER.delete_list(name)
    return redirect(url_for('dashboard'))
@APP.route('/Add_items', methods=['POST', 'GET'])
@authorisation
def add_items():
    """Adds items to list"""
    if request.method == 'POST':
        listname = request.form['listname']
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        item = Item(name, description, price)
        list_ = USER.get_list(listname)
        list_.add_item(name, item)
    return render_template("edit_shoppinglist.html")
@APP.route('/remove_items', methods=['POST', 'GET'])
@authorisation
def remove_item():
    """Method to remove itmems from lists"""
    if request.method == 'POST':
        listname = request.form['listname']
        name = request.form['name']
        list_ = USER.get_list(listname)
        list_.remove_item(name)
    return render_template("edit_shopiing.html")
@APP.route('/update_list', methods=['POST', 'GET'])
@authorisation
def update_list():
    if request.method == 'POST':
        name = request.args.get('name')
        
        USER.update_list()