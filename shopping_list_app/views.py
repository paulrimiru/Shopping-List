"""
Class for rendering my views in template folder
"""
from flask import render_template

from shopping_list_app import APP

@APP.route('/')
def index():
    """
    Render the index page
    """
    return render_template("index.html")

@APP.route('/dashboard/')
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
    return render_template("Login.html")

@APP.route('/register/')
def register():
    """
    Render Register page used to sign up the user
    """
    return render_template("register.html")

@APP.route('/create_shoppinglist/')
def create_shoppinglist():
    """
    Render view for creating new shopping lists
    """
    return render_template("create_shoppinglist.html")

@APP.route('/edit_shoppinglist/')
def edit_shoppinglist():
    """
    Render view for editing shopping lists
    """
    return render_template("edit_shoppinglist.html")
