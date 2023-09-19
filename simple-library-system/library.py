import time
from colorama import Fore, Style

# List of objects to store books
books = [
    {
        "id": 1,
        "name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "borrowed": False,
        "borrower": "",
    },
    {
        "id": 2,
        "name": "1984",
        "author": "George Orwell",
        "borrowed": False,
        "borrower": "",
    },
    {
        "id": 3,
        "name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "borrowed": False,
        "borrower": "",
    },
    {
        "id": 4,
        "name": "Pride and Prejudice",
        "author": "Jane Austen",
        "borrowed": False,
        "borrower": "",
    },
    {
        "id": 5,
        "name": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "borrowed": False,
        "borrower": "",
    },
]

# Students list which will store information such as the books borrowe by a student, and due dates etc...
students = [{}]


def main():
    user_choice = ""
    options = ["Borrow a book", "Return a book", "Find a book"]
    print("Welcome to the Student Library!\n")
    time.sleep(1)

    input_message = "What would you like to do?\n"

    for index, option in enumerate(options):
        input_message += f"{index+1}) {option}\n"

    # Starts a while loop that continues as long as the user's choice is not one of the valid choices.
    while user_choice not in map(str, range(1, len(options) + 1)):
        user_choice = input(input_message)

    if user_choice == "1":
        time.sleep(1)
        book_choice = input("Enter the name of the book you would like to borrow: ")
        for book in books:
            if book["name"].lower() == str(book_choice).lower():
                time.sleep(2)
                print_book_info(book)


# Function to output book information in a user-friendly manner.
def print_book_info(book):
    print(f'Book name: {book["name"]}\nAuthor: {book["author"]}')
    if book["borrowed"] == False:
        confirmation = input("Would you like to borrow this book? (y/n)")
        if confirmation == "y":
            book["borrowed"] = True
            book["borrower"] = "Test"
            time.sleep(2)
            print(book)
            main()
        else:
            main()
    else:
        print(
            f"{Fore.RED}This book is not currently available, reason: borrowed by someone else.{Style.RESET_ALL}\nRedirecting to the main menu..."
        )
        time.sleep(5)
        main()


if (__name__) == "__main__":
    main()
