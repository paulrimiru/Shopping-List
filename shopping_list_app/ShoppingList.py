class ShoppingList(object):
    """This class adds  and removes items from a list"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = {}
    def add_item(self, name, item):
        """method for adding items to list"""
        self.items.update({name:item})
    def remove_item(self, item_name):
        """method to remove items from list"""
        self.items.pop(item_name)
    def update_item(self, item_name, newitem):
        """method to update and item in the list"""
        self.remove_item(item_name)
        self.add_item(newitem.name, newitem)
    def display_list(self):
        """returns list of all items in list"""
        return self.items
    def get_item(self, item_name):
        """returns a specific item in the list"""
        return self.items[item_name]
