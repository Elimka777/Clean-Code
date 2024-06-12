# main.py
from book.book import Book, display_book_info, change_book_price, update_book_stock

def main():
    book1 = Book("Harry Potter", "J. K. Rowling", 12.99, 5)
    display_book_info(book1)
    change_book_price(book1, 15.99)
    update_book_stock(book1, 2)
    display_book_info(book1)

if __name__ == "__main__":
    main()
