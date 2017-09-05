"""
    This class adds new user and manages the user's lists
"""
class User(object):
    """ This class manages user's lists"""
    def __init__(self):
        self.firstname = "firstname"
        self.secondname = "secondname"
        self.username = "firstname" +" "+ "secondname"
        self.email = "email"
        self.password = "password"
        self.userlists = []
    def instastiate_user(self, firstname, secondname, email, password):
        """This method instantiates a user"""
        self.firstname = firstname
        self.secondname = secondname
        self.username = firstname +" "+ secondname
        self.email = email
        self.password = password
    def create_list(self, mylist):
        """Creates a new user list"""
        self.userlists.append({mylist.name: mylist})
    def delete_list(self, name):
        """deletes a user list"""
        self.userlists.pop(name)
    def update_list(self, name, newlist):
        """updates a user list"""
        status = {}
        if name in self.userlists:
            status.update({"Success":False})
            status.update({"message":"List with same name exists"})
            return status
        else:
            templst = self.userlists[name]
            
            self.delete_list(name)
            self.create_list(newlist)
    def get_list(self, name):
        """gets a specific list"""
        return self.userlists[name]
    def get_all(self):
        """gets all the users lists"""
        return self.userlists
