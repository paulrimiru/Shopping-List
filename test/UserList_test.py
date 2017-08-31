"""module to test User ability to manipulate lists"""
import unittest

from shopping_list_app.User import User
from shopping_list_app.ShoppingList import ShoppingList

class UserListtest(unittest.TestCase):
    """Classs to test the manipulation of user list"""
    def setUp(self):
        self.user = User("Mike", "Paul", "mikepaul@shoppilist.com", 123456789)
    def test_create_new_list(self):
        """method to test creation of a new list"""
        newlist = ShoppingList("Week1", "Shopping requireed in week 1 andela")
        self.assertEqual(0, len(self.user.get_all()))
        self.user.create_list(newlist)
        self.assertEqual(1, len(self.user.get_all()))
        self.assertEqual("Week1", self.user.get_list(newlist.name).name)
    def test_remove_list(self):
        """method to test deletion of a list"""
        list1 = ShoppingList("Week2", "Shopping requireed in week 2 andela")
        list2 = ShoppingList("Week3", "Shopping requireed in week 3 andela")
        self.user.create_list(list1)
        self.user.create_list(list2)
        self.assertEqual(2, len(self.user.get_all()))
        self.user.delete_list(list1.name)
        self.assertEqual(1, len(self.user.get_all()))
    def test_update_list(self):
        """method to test update of a list"""
        list1 = ShoppingList("Week2", "Shopping requireed in week 2 andela")
        list2 = ShoppingList("Week3", "Shopping requireed in week 3 andela")
        self.user.create_list(list1)
        self.user.create_list(list2)
        self.assertEqual(2, len(self.user.get_all()))
        newlist1 = ShoppingList("Week 2", "Shopping requireed in week 4 andela")
        self.user.update_list(list1.name, newlist1)
        self.assertEqual("Shopping requireed in week 4 andela"
                         , self.user.get_list("Week 2").description)
