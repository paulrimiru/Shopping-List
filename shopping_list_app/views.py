"""
Class for rendering my views in template folder
"""
from functools import wraps
from flask import session, render_template, redirect, url_for, request, flash

from shopping_list_app import APP
from shopping_list_app.user import User
from shopping_list_app.admin import Admin
from shopping_list_app.shoppinglist import ShoppingList
from shopping_list_app.item import Item

ADMIN = Admin()
USER = None

def authorisation(func):
    """Wrapper to check user authorization"""
    @wraps(func)
    def auth(*args, **kargs):
        """checks for if the user is logged in through the session"""
        if "signed_in" not in session:
            return render_template("login.html", error="You need to be logged in")
        return func(*args, **kargs)
    return auth
@APP.route('/')
@APP.route('/index')
def index():
    """
    Render the index page
    """
    return render_template("index.html", user=USER)

@APP.route('/dashboard/<username>/<email>')
@authorisation
def dashboard(username, email):
    """
    Render the user dashboard
    """
    user_shoppinglist = []
    user_shoppingdict = ADMIN.get_user(email).get_all()
    for shoppinglist_name in user_shoppingdict:
        if user_shoppingdict.get(shoppinglist_name).useremail == email:
            user_shoppinglist.append(user_shoppingdict.get(shoppinglist_name))

    return render_template("dashboard.html", shoppinglistdict=user_shoppinglist,
                           username=username, email=email)

#CRUD and other logic for user
@APP.route('/logout/')
def logout():
    """LOgs out user"""
    session.pop('signed_in', None)
    return redirect(url_for("index"))

@APP.route('/create_user', methods=['POST', 'GET'])
def create_user():
    """Method retrieves data from post request and creates a user"""
    if request.method == 'POST':
        fname = request.form['firstname']
        sname = request.form['secondname']
        email = request.form['email']
        password = request.form['password']

        user = User(fname, sname, email, password)
        status = ADMIN.add_user(user)
        if status == "Registered successfully":
            session["signed_in"] = True
            return redirect(url_for('authenticate'))
        return redirect(url_for('index'))
    return render_template("register.html")
@APP.route('/authenticate', methods=['POST', 'GET'])
def authenticate():
    """Authenticates the user before login"""
    user_shoppinglist = []
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        status = ADMIN.check_password(email, password)
        if status['success']:
            session['email'] = email
            session['signed_in'] = True
            global USER
            USER = ADMIN.get_user(email)
            user = ADMIN.get_user(email)
            user_shoppingdict = user.get_all()
            for shoppinglist_name in user_shoppingdict:
                if user_shoppingdict.get(shoppinglist_name).useremail == email:
                    user_shoppinglist.append(user_shoppingdict.get(shoppinglist_name))
            return redirect(url_for('dashboard', username=status['username'],
                                    shoppinglist=user_shoppinglist, email=email))
        else:
            if status.get('has_account'):
                return status.get("message")
            else:
                return redirect(url_for('create_user'))
    elif request.method == 'GET':
        return render_template("login.html")
#CRUD and other logic for shopping lists
@APP.route('/create_shoppinglist/')
@authorisation
def create_shoppinglist():
    """
    Render view for creating new shopping lists
    """
    return render_template("create_shoppinglist.html", useremail=session['email'])

@APP.route('/createlist', methods=['POST', 'GET'])
@authorisation
def createlist():
    """creates a list for a user"""
    user_shoppinglist = []
    if request.method == 'POST':
        user_email = request.form['email']
        lname = request.form['listname']
        ldesc = request.form['description']
        shoppinglist_object = ShoppingList(user_email, lname, ldesc)
        ADMIN.get_user(user_email).create_list(shoppinglist_object)
        user_shoppingdict = ADMIN.get_user(user_email).get_all()
        for shoppinglist_name in user_shoppingdict:
            if user_shoppingdict.get(shoppinglist_name).useremail == user_email:
                user_shoppinglist.append(user_shoppingdict.get(shoppinglist_name))
    return render_template("dashboard.html", shoppinglist=user_shoppinglist, list_name=lname,
                           username=USER.username, email=user_email)

@APP.route('/edit_shoppinglist/<username>/<list_name>/<email>')
@authorisation
def edit_shoppinglist(username, list_name, email):
    """
    Render view for editing shopping lists
    """
    shoppinglist = USER.get_list(list_name)
    return render_template("edit_shoppinglist.html", description=shoppinglist.description,
                           list_name=list_name, username=username, email=email)

@APP.route('/remove_lists/<username>/<list_name>/<email>')
@authorisation
def remove_list(username, list_name, email):
    """Removes lists from users"""
    USER.delete_list(list_name)
    shopping_lists = USER.get_all()
    user_shoppinglist = []

    for key in shopping_lists:
        if shopping_lists[key].useremail == USER.email:
            user_shoppinglist.append(shopping_lists[key])
    return render_template("dashboard.html", shoppinglist=user_shoppinglist,
                           username=username, email=email)

@APP.route('/update_list', methods=['POST', 'GET'])
@authorisation
def update_list():
    """Method updates the list details"""
    if request.method == 'POST':
        listnname = request.form["current"]
        listnewname = request.form["listname"]
        listdescription = request.form["description"]

        newshoppinglist = ShoppingList(USER.email, listnewname, listdescription)
        USER.update_list(listnname, newshoppinglist)

        shopping_lists = USER.get_all()
        user_shoppinglist = []

        for key in shopping_lists:
            if shopping_lists[key].useremail == USER.email:
                user_shoppinglist.append(shopping_lists[key])
    return render_template("dashboard.html", shoppinglist=user_shoppinglist,
                           username=USER.username, email=USER.email)
#CRUD and other logic for items
@APP.route('/add_itemstolist/<username>/<list_name>/<email>')
@authorisation
def additems_tolist(username, list_name, email):
    """
    Render view for editing shopping lists
    """
    shoppinglist = USER.get_list(list_name)
    return render_template("additems_tolist.html",
                           shoppinglist=shoppinglist.display_list(),
                           list_name=list_name, username=username, email=email)

@APP.route('/add_items', methods=['POST', 'GET'])
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
        shoppinglist = USER.get_list(listname)
    return render_template("additems_tolist.html", list_name=listname,
                           shoppinglist=shoppinglist.display_list(), username=USER.username,
                           email=USER.email)

@APP.route('/view_items/<listname>/<email>', methods=['POST', 'GET'])
@authorisation
def view_items(listname, email):
    """view items in list"""
    shoppinglist = USER.get_list(listname)
    return render_template("view_items.html", list_name=listname,
                           shoppinglist=shoppinglist.display_list(), username=USER.username,
                           useremail=email)

@APP.route('/add_itemsview/<username>/<list_name>/<email>', methods=['POST', 'GET'])
@authorisation
def additems_view(username, list_name, email):
    """Renders the page to add items to list"""
    return render_template("additems_tolist.html", list_name=list_name, username=username,
                           useremail=email)

@APP.route('/remove_items/<item_name>/<list_name>/<email>', methods=['POST', 'GET'])
@authorisation
def remove_item(item_name, list_name, email):
    """Method to remove itmems from lists"""
    list_ = USER.get_list(list_name)
    list_.remove_item(item_name)
    return render_template("additems_tolist.html", list_name=list_name,
                           shoppinglist=list_.display_list(), useremail=email)
# custom error pages
@APP.errorhandler(404)
def page_not_found_error(error):
    """Renders page if request is not found"""
    return render_template("404.html"), 404

@APP.errorhandler(500)
def internal_server_error(error):
    """Renders page if there is internal service error"""
    return render_template("500.html"), 500
