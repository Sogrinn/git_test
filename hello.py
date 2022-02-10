class Book:
    num_of_recursion = 0
    default_pages = 10

    def __init__(self, pages=default_pages):
        self.current_page = 0
        self.pages = pages
        self.additional_book = self.create_additional_book()

    def read_one_more_page(self):
        if self.current_page < self.pages:
            self.current_page += 1
            return True
        return False

    @classmethod
    def create_additional_book(cls):
        if cls.num_of_recursion > 10:
            cls.num_of_recursion = 0
        cls.num_of_recursion += 1
        if cls.num_of_recursion > 10:
            return False
        return cls(pages=300)

    @classmethod
    def change_default_pages_using_classmethod(cls, new_default_pages):
        cls.default_pages = new_default_pages
        return True


harry_potter = Book()
print(harry_potter.additional_book)