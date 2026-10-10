# Kyle Dinkins
# 10OCT2026
# DEV128 18807
# LA1: Lab Activity 1 - Invoice Due Date Program

from datetime import date, datetime, timedelta

# Gets input from the user for an invoice date and validates the format.
def get_invoice_date():
    while True:
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ")    
        try:
            invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%Y").date()
            if invoice_date > date.today():
                print("\nThe invoice date should not be in the future. Please enter a date for today or earlier.\n")
                continue
            return invoice_date
        except ValueError:
            print("\nInvalid entry. Please try again with the date's format as MM/DD/YYYY.\n")

# Outputs the program's title and continuously calculates the due date for the invoice until the user doesn't input 'y' or 'Y'.
def main():
    print("\nThe Invoice Due Date program")
    print("============================")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # Calculates the due date and the days overdue.
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today()
        days_overdue = (current_date - due_date).days

        # Display the invoice date, due date, current date, and days due/overdue.
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # Gets input from the user to see if they want to continue.
        again = input("Continue? (y/n): ")
        print()

    # Gives a farewell to the user, thanking them for using the program.
    print("Thank you for using The Invoice Due Date program!")      

if __name__ == "__main__":
    main()