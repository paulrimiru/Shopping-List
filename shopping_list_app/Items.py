class Items(object):
    """
    This class will create new items, delete items and update items
    """
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        