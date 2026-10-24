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
            print("size must be Small, Medium, or Large")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and not isinstance(value, bool) and value >= 0:
            self._price = float(value)
        else:
            print("price must be a non-negative number")

    def tip(self):
        self.price += 1
        print("This coffee is great, here\u2019s a tip!")
        return self.price

    def __str__(self):
        return f"{self.size} coffee (${self.price:.2f})"

    def __repr__(self):
        return f"Coffee('{self.size}', {self.price})"