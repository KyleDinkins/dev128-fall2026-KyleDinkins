# Kyle Dinkins
# 17OCT2026
# DEV128 18807
# LA3: Lab Activity 3 - Objects

# Import dataclass for cleaner classes
from dataclasses import dataclass

# Creates a "Product" class with methods to calculate discounted price
@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:int = 0

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

    def getDescription(self):
        return self.name

# Creates a "Media" class with a "format" string attribute
@dataclass
class Media(Product):
    format:str = ""

# Creates a "Book" class to display the name of the book and author
@dataclass
class Book(Media):
    author:str = ""

    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.author}"

# Creates a "Movie" class to display the name of the movie and the year
@dataclass        
class Movie(Media):
    year:int = 0

    def getDescription(self):
        return f"{Product.getDescription(self)} ({self.year})"

# Creates an "Album" class to display the name of the album and the artist
@dataclass        
class Album(Media):
    artist:str = ""

    def getDescription(self):
        return f"{Product.getDescription(self)} by {self.artist}"