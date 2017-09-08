"""Test modelu fo Admin.py"""
import unittest

from shopping_list_app.admin import Admin
from shopping_list_app.user import User

class AdminTest(unittest.TestCase):
    """class containing tests for admin.py methods"""
    def setUp(self):
        self.admin = Admin()
        self.user = User("Mike", "Paul", "mikepaul@shoppilist.com", 123456789)
    def test_add_user(self):
        """test to add a user"""
        myuser = User("Mike", "Paul", "mikepaul@shoppilist.com", 123456789)
        self.admin.add_user(myuser)

        self.assertEqual(1, len(self.admin.get_all_users()))
    def test_remove_user(self):
        """test to remove a user"""
        reception = User("Mike", "Paul", "mikepaul@shoppilist.com", 123456789)
        self.admin.add_user(reception)
        self.assertEqual(1, len(self.admin.get_all_users()))
        self.admin.remove_user("mikepaul@shoppilist.com")
        self.assertEqual(0, len(self.admin.get_all_users()))
    def test_update_user(self):
        """test to determine if user is updated"""
        myuser = User("Mike", "Paul", "mikepaul@shoppilist.com", 123456789)
        self.admin.add_user(myuser)
        self.assertEqual(1, len(self.admin.get_all_users()))

        newuser = User("Mike", "Paul", "mikepaul@shoppilist.com", 123456789)
        self.admin.update_user(
            myuser.email, newuser)

        self.assertEqual(newuser.firstname, self.admin.get_user(newuser.email).firstname)
if __name__ == '__main__':
    unittest.main()
