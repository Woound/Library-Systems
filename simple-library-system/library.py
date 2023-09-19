import time

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


# Function to handle what the user would like to do
def welcome():
    user_choice = ""
    print("Welcome to the Student Library!")
    time.sleep(1)

    input_message = "What would you like to do?\n"

    for index, option in enumerate(options):
        input_message += f"{index+1}) {option}\n"

    # Starts a while loop that continues as long as the user's choice is not one of the valid choices.
    while user_choice not in map(str, range(1, len(options) + 1)):
        user_choice = input(input_message)

    return user_choice


# Function to output book information in a user-friendly manner.
def print_book_info(book):
    print(f'Book name: {book["name"]}\nAuthor: {book["author"]}')


# Students list which will store information such as the books borrowe by a student, and due dates etc...
students = [{}]
options = ["Borrow a book", "Return a book", "Find a book"]

user_choice = welcome()
if user_choice == "1":
    time.sleep(1)
    book_choice = input("Enter the name of the book you would like to borrow: ")
    for book in books:
        if book["name"].lower() == str(book_choice).lower():
            print_book_info(book)
