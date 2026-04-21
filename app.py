print("Menu:\n")
print("1. View Books, 2. Add book, 3. Borrow book, 4. Return book, 5. Search book, 6. Exit")

books = {}
borrowed = {}


def add_books():
    while True:
        book = input(
            "Enter names of books you have (q to quit): ").strip().lower()

        if book.lower() == 'q':
            break

        if book in books:
            books[book] += 1
        else:
            books[book] = 1

        print("Book added successfully.")


def borrow_books():
    book = input("Enter book name to borrow: ").strip().lower()
    if book not in books:
        print("Book not found")
        return

    available = books[book] - borrowed.get(book, 0)
    if available <= 0:
        print("No copies available")
        return

    qty = int(input("How many copies to borrow: "))
    if qty > available:
        print("Not enough copies available")
        return

    if book in borrowed:
        borrowed[book] += qty
    else:
        borrowed[book] = qty

    print("Book borrowed successfully")


# Books are saved in the file
def save_library():
    with open("library_books.txt", "w") as f:
        f.write("Total Books:\n")
        for book, qty in books.items():
            f.write(f"{book} - {qty}\n")

        f.write("\nBorrowed Books: \n")
        for book, qty in borrowed.items():
            f.write(f"{book} - {qty}\n")
        f.write("\nAvailable Books: \n")
        for book, qty in books.items():
            issued = borrowed.get(book, 0)
            available = qty - issued
            f.write(f"{book} - {available}\n")


def view_books():
    with open("library_books.txt") as f:
        return f.read()


def return_books():
    book = input("enter book name to return: ").strip().lower()
    qty = int(input("enter the number of books to return: "))
    if book not in borrowed:
        print("this book is not currently borrowed.")
    else:
        if qty > borrowed[book]:
            print("invalid number of books.")
        else:
            borrowed[book] -= qty
            if borrowed[book] == 0:
                del borrowed[book]
    print("Book returned successfully")


def search_books():
    book = input("search a book by name: ").strip().lower()
    if book in books:
        total = books[book]
        issued = borrowed.get(book, 0)
        available = total - issued
        print("Book Found:")
        print("Total Books:", total)
        print("Borrowed Books:", issued)
        print("Available Books:", available)
    else:
        print("Book not found.")


def choices():
    while True:
        user_choice = input(
            "Enter 1 to add, 2 to view books, 3 to borrow books, 4 to return books,5 to search a book and 6 to exit: ")

        if user_choice == "1":
            add_books()
            save_library()
        elif user_choice == "2":
            print(view_books())
        elif user_choice == "3":
            borrow_books()
            save_library()
        elif user_choice == "4":
            return_books()
            save_library()
        elif user_choice == "5":
            search_books()
        elif user_choice == "6":
            print("Thanks for using library!")
            break
        else:
            print("Choose from the given choices.")


choices()
