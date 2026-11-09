# Kyle Dinkins
# 25OCT2026
# DEV128 18807
# Programming Project 1: SQLite Database App

# import the sqlite3 database module
import sqlite3

def setup_db(conn, cursor):
    # check if the user table already exists, if so, drop it so we can start with a new table
    cursor.execute("DROP TABLE IF EXISTS user;")

    # create the table if it doesn't already exist
    # note that primary keys are automatically created in sqlite3 and referenced as rowid
    cursor.execute("CREATE TABLE user (first_name TEXT, last_name TEXT, email TEXT, phone TEXT, street_address TEXT, city TEXT, state TEXT, zip_code TEXT)")

    # create some records of data
    cursor.execute("INSERT INTO user VALUES (\"Tony\", \"Stark\", \"ironman@stark.com\", \"555-111-2222\", \"12345 Main Street\", \"Malibu\", \"CA\", \"98581\")")
    cursor.execute("INSERT INTO user VALUES (\"Carol\", \"Danvers\", \"marvel@stark.com\", \"555-123-2424\", \"1233 Michigan Ave.\", \"Boston\", \"MA\", \"00248\")")
    cursor.execute("INSERT INTO user VALUES (\"Bruce\", \"Banner\", \"hulk@stark.com\", \"555-143-7892\", \"5200 Old Santa Fe Trl\", \"Santa Fe\", \"NM\", \"87505\")")
    cursor.execute("INSERT INTO user VALUES (\"Stephen\", \"Strange\", \"doctorstrange@stark.com\", \"555-742-1092\", \"177A Bleecker Street\", \"New York City\", \"NY\", \"10012\")")
    cursor.execute("INSERT INTO user VALUES (\"Natasha\", \"Romanoff\", \"blackwidow@stark.com\", \"555-234-8506\", \"3278 Embry Hills Drive\", \"Chamblee\", \"GA\", \"30341\")")

    return cursor

def list_names(conn, cursor):
    # create a cursor that we will use to move through the database
    cursor = conn.cursor()

    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name FROM user")

    # store the results of the query to a list called users
    users = cursor.fetchall()

    # now we can loop through the results of the query
    for this_user in users:
        print(this_user[0], this_user[1], this_user[2])
    print()
    return cursor

def list_contact_info(conn, cursor):
    # create a cursor that we will use to move through the database
    cursor = conn.cursor()

    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, phone, email FROM user")

    # store the results of the query to a list called users
    users = cursor.fetchall()

    # now we can loop through the results of the query
    for this_user in users:
        print(this_user[0], this_user[1], this_user[2], this_user[3], this_user[4])
    print()
    return cursor

def list_location(conn, cursor):
    # create a cursor that we will use to move through the database
    cursor = conn.cursor()

    # query the table including the rowid primary key value
    cursor.execute("SELECT rowid, first_name, last_name, street_address, city, state, zip_code FROM user")

    # store the results of the query to a list called users
    users = cursor.fetchall()

    # now we can loop through the results of the query
    for this_user in users:
        print(this_user[0], this_user[1], this_user[2], this_user[3], this_user[4], this_user[5], this_user[6])
    print()
    return cursor

def add_user(conn, cursor):
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

    sql = """
        INSERT INTO user (first_name, last_name, email, phone, street_address, city, state, zip_code)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

    cursor.execute(sql, (input_first_name, input_last_name, input_email, input_phone, input_street_address, input_city, input_state, input_zip_code))

    print()
    print(input_first_name, "added! Thank you.\n")
    return cursor

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


def main():
    # create a connection to the database file
    conn = sqlite3.connect("myDatabase.db")
    
    # create a cursor that we will use to move through the database
    cursor = conn.cursor()

    while True:
        menu()
        choice = input("\nSelect your option: ")
        print()
        if choice == "0":
            cursor = setup_db (conn, cursor)
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

    print("Thank you for using the Marvel Database!")



if __name__ == "__main__":
    main()