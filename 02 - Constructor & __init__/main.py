#--------------------------------------------------------------------#
# Second program: Constructor and __init__
# Created by: Jim - https://www.youtube.com/watch?v=uJWhQAHaP_M
# Changed by: Thiago Piovesan
# Objective: Learning about contructor and __init__
#--------------------------------------------------------------------#
class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equals to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equals to 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    # Function to calculate the total price
    def calculate_total_price(self):
        return self.price * self.quantity
#--------------------------------------------------------------------#
item1 = Item("Phone", 100, 4)
item2 = Item("Laptop", 1000, 12)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

#--------------------------------------------------------------------#