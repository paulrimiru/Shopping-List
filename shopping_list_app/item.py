"""This module will be used to initialise items object"""
class Item(object):
    """
    This class will be used to initialise item objects
    """
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        