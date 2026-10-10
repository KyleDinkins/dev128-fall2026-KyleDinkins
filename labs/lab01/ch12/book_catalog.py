# Kyle Dinkins
# 10OCT2026
# DEV128 18807
# LA1: Lab Activity 1 - Book Catalog Program

# Lists all books in the catalog.
def list_books(book_catalog):
    for book in book_catalog:
        print(book)

# Allows the user to access a book in the catalog regardless of capitalization.
def find_book_key(book_catalog, search_title):
    for book in book_catalog:
        if book.lower() == search_title.lower():
            return book
    return None

# Gets input from the user and returns information about the corresponding book.
def show_book(book_catalog):
    title = input("Title: ")
    print()
    key_match = find_book_key(book_catalog, title)
    if key_match:
        book_info = book_catalog[key_match]
        print(f"Title:    {key_match}")
        print(f"Author:   {book_info['author']}")
        print(f"Pub year: {book_info['pubyear']}")
    else:
        print(f"Sorry, {title} doesn't exist in the catalog.")

# Gets input from the user to add new book information to the catalog or edit book information in the catalog.
def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    key_match = find_book_key(book_catalog, title)
    if mode == "add" and key_match:
        print(f"{title} already exists in the catalog.")
        response = input ("Would you like to edit it? (y/n): ").lower()
        if(response != "y"):
            return
        title = key_match
    elif mode == "edit" and not key_match:
        print(f"{title} doesn't exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if (response != "y"):
            return
    # Makes sure a new book isn't added to the catalog if capitalization differs.
    elif mode == "edit" and key_match:
        title = key_match

    # Gets the remaining book data and creates a dictionary for the data.
    print()
    author = input("Author name: ")
    print()
    pubyear = input("Publication year: ")
    book = {title: {"author": author, "pubyear": pubyear}}

    # Adds the book data to the catalog using the update operator.
    book_catalog |= book

# Gets input from the user and deletes the corresponding book information from the catalog.
def delete_book(book_catalog):
    title = input("Title: ")
    key_match = find_book_key(book_catalog, title)
    if key_match:
        del book_catalog[key_match]
        print(f"\n{key_match} removed from catalog.")
    else:
        print(f"\n{title} doesn't exist in the catalog.")

# Displays the command menu.
def display_menu():
    print("\n========================")
    print("COMMAND MENU")
    print("list - List books")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")
    print("========================")

# Allows the user to choose between multiple commands and continues until the user types "exit".
def main():
    print("\nThe Book Catalog Program")
    book_catalog = {
        "Moby Dick": 
            {"author" : "Herman Melville",
             "pubyear" : "1851"},
        "The Hobbit":
            {"author" : "J. R. R. Tolkien", 
             "pubyear" : "1937"},
        "Slaughterhouse Five":
            {"author" : "Kurt Vonnegut",
             "pubyear" : "1969"}
        }
    while True:
        display_menu()
        print()
        command = input("Command: ").lower()
        print()
        if command == "list":
            list_books(book_catalog)
        elif command == "show":
            show_book(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Thank you for using Book Catalog Program, goodbye!\n")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()