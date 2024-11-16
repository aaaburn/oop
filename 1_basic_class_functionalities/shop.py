class Shop():
    """This is shop class."""

    def __init__(self, name:str, items:list):
        self.name = name
        self.items = items

    def get_items_count(self):
        return len(self.items)


# Execute example
shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())



