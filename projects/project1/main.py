# Kyle Dinkins
# 09NOV2026
# DEV128 18807
# Programming Project 1: SQLite Database App

# import the sqlite3 database module
import sqlite3


# Creates the database
def setup_db(conn, cursor):
    # creates the table if it doesn't already exist
    # note: primary keys are automatically created in sqlite3 and referenced as rowid
    cursor.execute("CREATE TABLE IF NOT EXISTS user (first_name TEXT, last_name TEXT, email TEXT, phone TEXT, street_address TEXT, city TEXT, state TEXT, zip_code TEXT)")

    # creates some records of data
    cursor.execute("INSERT INTO user VALUES (\"Tony\", \"Stark\", \"ironman@stark.com\", \"555-111-2222\", \"12345 Main Street\", \"Malibu\", \"CA\", \"98581\")")
    cursor.execute("INSERT INTO user VALUES (\"Carol\", \"Danvers\", \"marvel@stark.com\", \"555-123-2424\", \"1233 Michigan Ave.\", \"Boston\", \"MA\", \"00248\")")
    cursor.execute("INSERT INTO user VALUES (\"Bruce\", \"Banner\", \"hulk@stark.com\", \"555-143-7892\", \"5200 Old Santa Fe Trl\", \"Santa Fe\", \"NM\", \"87505\")")
    cursor.execute("INSERT INTO user VALUES (\"Stephen\", \"Strange\", \"doctorstrange@stark.com\", \"555-742-1092\", \"177A Bleecker Street\", \"New York City\", \"NY\", \"10012\")")
    cursor.execute("INSERT INTO user VALUES (\"Natasha\", \"Romanoff\", \"blackwidow@stark.com\", \"555-234-8506\", \"3278 Embry Hills Drive\", \"Chamblee\", \"GA\", \"30341\")")

    return cursor

def list_names(conn, cursor):
    # creates a cursor to move through the database
    cursor = conn.cursor()

    # queries the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name FROM user")

    # stores the results of the query to a list called users
    users = cursor.fetchall()

    print("Names of all users")
    print("------------------")

    # Loops through the results of the query and prints names in a numbered list
    for this_user in users:
        print(f"{this_user[0]:>2}. {this_user[1]} {this_user[2]}")
    print()
    return cursor

def list_contact_info(conn, cursor):
    # creates a cursor that to move through the database
    cursor = conn.cursor()

    # queries the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, phone, email FROM user")

    # stores the results of the query to a list called users
    users = cursor.fetchall()

    print("Contact information of all users")
    print("--------------------------------")

    # loops through the results of the query printing a numbered list of the names, phones, and emails of the users
    for this_user in users:
        full_name = f"{this_user[1]} {this_user[2]}"
        print(f"{this_user[0]:>2}. {full_name:<18} {this_user[3]:<14} {this_user[4]}")
    print()
    return cursor

def list_location(conn, cursor):
    # creates a cursor that to move through the database
    cursor = conn.cursor()

    # queries the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, street_address, city, state, zip_code FROM user")

    # stores the results of the query to a list called users
    users = cursor.fetchall()

    print("Addresses of all users")
    print("----------------------")

    # loops through the results of the query, printing a numbered list of the names and address of the users
    for this_user in users:
        full_name = f"{this_user[1]} {this_user[2]}"
        print(f"{this_user[0]:>2}. {full_name:<18} {this_user[3]}, {this_user[4]}, {this_user[5]} {this_user[6]}")
    print()
    return cursor

def add_user(conn, cursor):
    
    # Gets input to store information into the database for a new user
    print("Add New User")
    print("------------\n")
    input_first_name = input("First Name: ")
    input_last_name = input("Last Name: ")
    input_email = input("Email: ")
    input_phone = input("Phone Number: ")
    input_street_address = input("Street Address: ")
    input_city = input("City: ")
    input_state = input("State (2 Digits): ")
    input_zip_code = input("Zip Code: ")

    # Sets up the structure of the variables to be added to the database
    sql = """
        INSERT INTO user (first_name, last_name, email, phone, street_address, city, state, zip_code)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
    # Associates the user inputs to the variables to be added to the database for the new user
    cursor.execute(sql, (input_first_name, input_last_name, input_email, input_phone, input_street_address, input_city, input_state, input_zip_code))

    # Saves the data here in case the program crashes before the user exits
    conn.commit()

    # Confirmation message
    print()
    print(input_first_name, input_last_name, "added! Thank you.\n")
    return cursor

# Outputs the menu of actions the user can take
def menu():
    print("Marvel Database Menu")
    print("--------------------\n")
    print("Choose an option below:")
    print("0 - Initialize Database (Careful this will wipe all data!)")
    print("1 - list all names")
    print("2 - list Names, Phone, and Email")
    print("3 - list Names and Location")
    print("4 - Add New User")
    print("5 - Exit the program")

# Outputs the menu continuously, performing actions connected to the database associated with user inputs until the user inputs '5'
def main():
    # create a connection to the database file
    conn = sqlite3.connect("myDatabase.db")
    
    # create a cursor that we will use to move through the database
    cursor = conn.cursor()

    # Shows the user the menu and runs through actions associated with inputs until the user exits (inputs '5')
    while True:
        menu()
        
        # Gets input from the user for their menu selection
        choice = input("\nSelect your option: ")
        print()
        if choice == "0":

            # Warns the user that intiializing the database will wipe the current database
            print("WARNING: This will wipe all data!")
            
            # Gets input from the user to confirm database intiialization
            confirmation = input("\nType \"confirm\" to continue (or press Enter to cancel): ")

            # Initializes the database if the user input "confirm"
            if confirmation.strip().lower() == "confirm":
                cursor = setup_db (conn, cursor)
                # Outputs database intialization confirmation
                print("\nDatabase initialized successfully.\n")
            else:
                # Outputs the action was canceled
                print("\nAction canceled.\n")
        elif choice == "1":
            list_names(conn, cursor)
        elif choice == "2":
            list_contact_info(conn, cursor)
        elif choice == "3":
            list_location(conn, cursor)
        elif choice == "4":
            add_user(conn, cursor)
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")
    # save the updates to the database - if you don't commit any updates/inserts to the database will not be saved
    conn.commit()

    # close the connection
    conn.close()

    # Outputs a farewell message
    print("Thank you for using the Marvel Database!")

# If the main function is not imported, then the main function is ran.
if __name__ == "__main__":
    main()