import unittest

from shopping_list_app.ShoppingList import ShoppingList
from shopping_list_app.Items import Items

class ShoppingList_test(unittest.TestCase):
    def setUp(self):
        self.firstlist = ShoppingList("FirstList", "this is my first list sir")
        self.firstitem = Items("milk", "for the kid", 500)
    def test_adding_item(self):
        item = Items("Choclate", "For the wife", 1500)
        self.assertEqual(0, len(self.firstlist.items))
        self.firstlist.add_item("Choclate", item)
        self.assertEqual(1, len(self.firstlist.items))
    def test_remove_item(self):
        item = Items("Wheat Floor", "For cooking chapati", 240)
        item2 = Items("Maize floor", "For cooking ugali", 100)

        self.firstlist.add_item("Wheat Floor", item)
        self.firstlist.add_item("Maize Floor", item2)

        self.assertEqual(2, len(self.firstlist.items))
        self.firstlist.remove_item(item.name)
        self.assertEqual(1, len(self.firstlist.items))

if __name__ == '__main__':
    unittest.main()
    