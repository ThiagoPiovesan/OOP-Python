#--------------------------------------------------------------------#
# First program: Constructor and __init__
# Created by: Jim
# Changed by: Thiago Piovesan
#--------------------------------------------------------------------#

## First way - Not efficient:

# How to create a class:
# class Item:
#     def calculate_total_price(self, x, y):
#         return x * y

# # How to create an instance of a class
# item1 = Item()

# # Assign attributes:
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# # Calling methods from instances of a class:
# print(item1.calculate_total_price(item1.price, item1.quantity))

# # How to create an instance of a class (We could create as much as instances we'd like to)
# item2 = Item()

# # Assign attributes
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

# # Calling methods from instances of a class: 
# print(item2.calculate_total_price(item2.price, item2.quantity))
#--------------------------------------------------------------------#
class Item:
    pay_rate = 0.8                  # The pay rate after 20% discount
    all = []
    
    # Init:
    def __init__(self, name: str, price: float, quantity = 0) -> None:
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equals to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equals to 0"
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute:
        Item.all.append(self)
            
    # Function to calculate the total price
    def calculate_total_price(self) -> None:
        return self.price * self.quantity

    # Function to apply discount
    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate
          
    # Imprimir itens:
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"
#--------------------------------------------------------------------#

item1 = Item("Phone", 100, 3)
item2 = Item("Laptop", 2000, 2)
item3 = Item("Cable", 5, 10)
item4 = Item("Mouse", 60, 2)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
#--------------------------------------------------------------------#