import time
from colorama import Fore, Style

# List of book objects
books = [
    {
        "id": 1,
        "name": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "borrowed": False,
        "borrower": 0,
    },
    {
        "id": 2,
        "name": "1984",
        "author": "George Orwell",
        "borrowed": False,
        "borrower": 0,
    },
    {
        "id": 3,
        "name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "borrowed": False,
        "borrower": 0,
    },
    {
        "id": 4,
        "name": "Pride and Prejudice",
        "author": "Jane Austen",
        "borrowed": False,
        "borrower": 0,
    },
    {
        "id": 5,
        "name": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "borrowed": False,
        "borrower": 0,
    },
]

# Students list which will store information such as the books borrowed by a student, and due dates etc...
students = [
    {
        "student_id": 1001,
        "name": "Alice",
        "email": "alicewonderland@gmail.com",
        "books_borrowed": [],
    },
    {
        "student_id": 1002,
        "name": "Bob",
        "email": "bobthebuilder@gmail.com",
        "books_borrowed": [],
    },
]


def main():
    user_choice = ""
    options = ["Borrow a book", "Return a book", "Find a book"]
    print(f"\n{Fore.GREEN}Welcome to the Student Library!{Style.RESET_ALL}\n")
    time.sleep(1)

    input_message = "What would you like to do?\n"

    for index, option in enumerate(options):
        input_message += f"{index+1}) {option}\n"

    # Starts a while loop that continues as long as the user's choice is not one of the valid choices.
    while user_choice not in map(str, range(1, len(options) + 1)):
        user_choice = input(input_message)

    # Borrowing process
    if user_choice == "1":
        time.sleep(1)
        book_choice = input("Enter the name of the book you would like to borrow: ")
        for book in books:
            if book["name"].lower() == str(book_choice).lower():
                time.sleep(2)
                handle_borrowing(book)
        time.sleep(2)
        print(
            f"\n{Fore.RED}Book not found. Make sure the name is spelt correctly and try again!{Style.RESET_ALL}\nRedirecting to the main menu...\n"
        )
        time.sleep(2)
        main()

    # Returning process
    elif user_choice == "2":
        student_number = input("\nPlease enter your student id number: ")
        student_email = input("Please enter your email: ")
        for student in students:
            if (
                str(student["student_id"]) == student_number
                and student["email"] == student_email
            ):
                if len(student["books_borrowed"]) == 0:
                    print(
                        f"\n{Fore.LIGHTYELLOW_EX}You have no borrowed books.{Style.RESET_ALL}"
                    )
                    print("\nRedirecting to main menu...")
                    time.sleep(3)
                    main()

                return_choice = ""
                borrowed_list = "\nWhich book would you like to return?\n"

                for index, borrowed in enumerate(student["books_borrowed"]):
                    borrowed_list += f"{index+1}) {borrowed}\n"
                while return_choice not in map(
                    str, range(1, len(student["books_borrowed"]) + 1)
                ):
                    return_choice = input(borrowed_list)
                student["books_borrowed"].pop(int(return_choice) - 1)
                time.sleep(3)
                print(
                    f"\n{Fore.LIGHTMAGENTA_EX}Your book has succesfully been returned. Thank you!{Style.RESET_ALL}"
                )
                time.sleep(2)
                main()
            else:
                time.sleep(1)

                print(
                    f"{Fore.RED}Student not found, please check your details and try again. Redirecting to the main menu...{Style.RESET_ALL}\n"
                )
                time.sleep(2)
                main()

    # Looking-up process
    elif user_choice == "3":
        while True:
            book_choice = input(
                "Enter the name of the book you would like to find or (n) to exit: "
            )
            if book_choice == "n":
                break
            for book in books:
                if book["name"].lower() == str(book_choice).lower():
                    print(
                        f'Book name: {book["name"]}\nAuthor: {book["author"]}\nAvailable to borrow: {not book["borrowed"]}'
                    )
                    time.sleep(2)
                    main()
            print(
                f"\n{Fore.RED}Book not found. Make sure the name is spelt correctly and try again!{Style.RESET_ALL}\n"
            )
            time.sleep(2)
        main()


# Function to handle borrowing process of the system
def handle_borrowing(book):
    print(f'Book name: {book["name"]}\nAuthor: {book["author"]}')
    if book["borrowed"] == False:
        confirmation = input("Would you like to borrow this book? (y/n)")
        while confirmation != "y" and confirmation != "n":
            confirmation = input(
                "Incorrect option: Would you like to borrow this book? (y/n)"
            )
        if confirmation == "y":
            student_number = input("\nPlease enter your student id number: ")
            student_email = input("Please enter your email to confirm: ")
            for student in students:
                if (
                    str(student["student_id"]) == student_number
                    and student["email"] == student_email
                ):
                    book["borrowed"] = True
                    book["borrower"] = int(student_number)
                    student["books_borrowed"].append(book["name"])
                    time.sleep(2)
                    print(
                        f"\n{Fore.LIGHTCYAN_EX}The book has been allocated to you succesfully. Enjoy.{Style.RESET_ALL}\n"
                    )
                    print(student)
                    print(book)
                    time.sleep(3)
                    main()
            time.sleep(1)
            print(
                f"{Fore.RED}Student not found, please check your details and try again. Redirecting to the main menu...{Style.RESET_ALL}\n"
            )
            time.sleep(2)
            main()
        elif confirmation == "n":
            main()
    else:
        print(
            f"\n{Fore.RED}This book is not currently available, reason: borrowed by someone else.\
                {Style.RESET_ALL}\nRedirecting to the main menu...\n"
        )
        time.sleep(5)
        main()


if (__name__) == "__main__":
    main()
