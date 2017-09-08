"""
This module adds users and removes users from the app
"""
import re
class Admin(object):
    """class adds and removes users"""
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """Method adds new user"""
        username = user.firstname+user.secondname
        if user.email in self.users:
            return "User already exists"
        else:
            if len(user.password) < 6:
                return "Password too short"
            elif not re.match("^[a-zA-Z0-9_]*$", username):
                return "Do not include special characters in your names"
            else:
                self.users.update({user.email:user})
                return "Registered successfully"
        return
    def remove_user(self, email):
        """method removes a user"""
        self.users.pop(email)
    def update_user(self, email, newuser):
        """method updates a users details"""
        self.remove_user(email)
        self.add_user(newuser)
    def get_all_users(self):
        """method returns all users"""
        return self.users
    def get_user(self, email):
        """method returns specific user"""
        return self.users[email]
    def check_password(self, email, password):
        """Checks if the password is correct"""
        account_details = {}
        if email in self.users:
            user = self.users[email]
            if user.password == password:
                account_details.update({"success":True})
                account_details.update({"message":"Welcome"})
                account_details.update({"username":user.username})
                return account_details
            else:
                account_details.update({"success":False})
                account_details.update({"message":"Wrong password"})
                return account_details
        else:
            account_details.update({"success":False})
            account_details.update({"message":"Please sign up first"})
            account_details.update({"has_account":False})
            return account_details

