"""
    This class adds new user and manages the user's lists
"""
from myapp.ShoppingList import ShoppingList
class User(object):
    def __init__(self, firstname, secondname, email, password):
        self.firstname = firstname
        self.secondname = secondname
        self.username = firstname + secondname
        self.email = email
        self.password = password
        self.userlists = {}
    def create_list(self, name, description):
        """Creates a new user list"""
        newlist = ShoppingList(name, description)
        self.userlists.update({name, newlist})
    def delete_list(self, name):
        """deletes a user list"""
        self.userlists.pop(name)
    def get_list(self, name):
        """gets a specific list"""
        return self.userlists[name]
