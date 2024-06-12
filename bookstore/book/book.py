# book/book.py

class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def update_title(self, new_title):
        self.title = new_title

    def update_author(self, new_author):
        self.author = new_author

    def update_price(self, new_price):
        self.price = new_price

    def update_stock(self, new_stock):
        self.stock = new_stock

    def check_availability(self):
        return self.stock > 0

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}, Stock: {self.stock}"

# Additional functions related to book management

def display_book_info(book):
    print(book)

def change_book_price(book, new_price):
    book.update_price(new_price)

def update_book_stock(book, new_stock):
    book.update_stock(new_stock)

# Example usage
if __name__ == "__main__":
    book1 = Book("Harry Potter", "J. K. Rowling", 12.99, 5)
    display_book_info(book1)
    change_book_price(book1, 15.99)
    update_book_stock(book1, 2)
    display_book_info(book1)
