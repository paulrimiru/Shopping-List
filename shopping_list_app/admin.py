"""
This module adds users and removes users from the app
"""
class Admin(object):
    """class adds and removes users"""
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """Method adds new user"""   
        self.users.update({user.email:user})
        print(vars(user))
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

