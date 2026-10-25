# Kyle Dinkins
# 17OCT2026
# DEV128 18807
# LA3: Lab Activity 3 - Product Viewer

# Imports custom classes for the program
from objects import Product, Media, Book, Movie, Album

# Displays a list of all the products
def show_products(products):
    print("PRODUCTS")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product.getDescription()}")
    print()

# Outputs a product description based on the type of product
def show_product(product):
    w=18
    print("PRODUCT DATA")
    print(f"{'Name:':{w}}{product.name}")
    if isinstance(product, Book):
        print(f"{'Author:':{w}}{product.author}")
    if isinstance(product, Movie):
        print(f"{'Year:':{w}}{product.year}")
    if isinstance(product, Album):
        print(f"{'Artist:':{w}}{product.artist}")
    if isinstance(product, Media):
        print(f"{'Format:':{w}}{product.format}")
    print(f"{'Discount price:':{w}}{product.getDiscountPrice():.2f}")
    print()

# Runs the program continuously until the user doesn't input "y"
def main():
    print("The Product Viewer Program")
    print("--------------------------")
    print()

    # Generates the objects for the products in the program
    products = (Product("Stanley 13 Ounce Wood Hammer", 12.99, 62),
                Book("The Big Short", 15.95, 34, "Hardcover", "Michael Lewis"),
                Book("You Are the One You’ve Been Waiting For", 18.45, 20, "Paperback", "Richard C. Schwartz"),
                Movie("The Holy Grail", 14.99, 68, "DVD", 1975),
                Movie("Good Will Hunting", 15.99, 40, "DVD", 1997),
                Album("Wish You Were Here", 31.99, 10, "Vinyl", "Pink Floyd"))
    show_products(products)


    choice = "y"
    while choice.lower() == "y":
        # Gets input from the user for a product number to be displayed
        number = int(input("Enter product number: "))
        print()

        product = products[number-1]
        show_product(product)

        choice = input("View another product? (y/n): ")
        print()

    # Outputs a farewell
    print("Thank you for using the Product Viewer program, goodbye!")

if __name__ == "__main__":
    main()
