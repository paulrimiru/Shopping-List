"""
    This class adds new user and manages the user's lists
"""
from shopping_list_app.ShoppingList import ShoppingList
class User(object):
    def __init__(self, firstname, secondname, email, password):
        self.firstname = firstname
        self.secondname = secondname
        self.username = firstname + secondname
        self.email = email
        self.password = password
        self.userlists = {}
    def create_list(self, mylist):
        """Creates a new user list"""
        self.userlists.update({mylist.email, mylist})
    def delete_list(self, email):
        """deletes a user list"""
        self.userlists.pop(email)
    def get_list(self, email):
        """gets a specific list"""
        return self.userlists[email]
    def get_all(self):
        """gets all the users lists"""
        return self.userlists
