# post lab 14:
# example : 1
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 * math.pi * self.radius

circle1 = Circle(15)
print("Area of circle:", circle1.area())
print("Perimeter of circle:", circle1.perimeter())


# example : 2
# Book class to store book details and handle discounts
class Book:
    # Constructor to initialize title, author, and price
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # Method to display book details
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

    # Method to apply a discount to the price
    def apply_discount(self, percent):
        discount_amount = self.price * (percent / 100)
        self.price -= discount_amount

# Create two book objects with different details
book1 = Book("Manvi Ni Bhavai", "pannalal patel", 389)
book2 = Book("Saraswatichandra", "Govardhanram Tripathi", 348)

# Display details of both books
print("\nBook 1 details:")
book1.display()
print("\nBook 2 details:")
book2.display()

# Apply 10% discount to book1 and display updated price
book1.apply_discount(10)
print("\nBook 1 details after 10% discount:")
book1.display()
