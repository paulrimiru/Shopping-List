"""
Class for rendering my views in template folder
"""
from flask import render_template

from app import app

@app.route('/')
def index():
    """
    Render the index page
    """
    return render_template("index.html")

@app.route('/dashboard/')
def dashboard():
    """
    Render the user dashboard
    """
    return render_template("dashboard.html")

@app.route('/Login/')
def login():
    """
    Render login page used to sign in
    """
    return render_template("Login.html")

@app.route('/register/')
def register():
    """
    Render Register page used to sign up the user
    """
    return render_template("register.html")

@app.route('/create_shoppinlist/')
def create_shoppinglist():
    """
    Render view for creating new shopping lists
    """
    return render_template("create_shoppinglist.html")

@app.route('/edit_shoppinglist/')
def edit_shoppinglist():
    """
    Render view for editing shopping lists
    """
    return render_template("edit_shoppinglist.html")
