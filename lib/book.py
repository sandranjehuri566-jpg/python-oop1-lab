class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._title = value
        else:
            print("title must be a non-empty string")

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
        return self.page_count + 1

    def __str__(self):
        return f"{self.title} ({self.page_count} pages)"

    def __repr__(self):
        return f"Book('{self.title}', {self.page_count})"