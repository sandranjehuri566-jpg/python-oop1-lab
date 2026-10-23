class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in ("Small", "Medium", "Large"):
            self._size = value
        else:
            raise ValueError("size must be 'Small', 'Medium', or 'Large'")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)):
            self._price = value
        else:
            raise ValueError("price must be a number")

    def tip(self):
        self.price += 1
        print("This coffee is great, here's a tip!")