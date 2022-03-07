#--------------------------------------------------------------------#
# Fourth program: Class vs Static Methods
# Created by: Jim - https://www.youtube.com/watch?v=XCgWYx-lGl8
# Changed by: Thiago Piovesan
# Objective: Learning the difference Class and Static methods.
#--------------------------------------------------------------------#

# Libs importations
import csv
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
        
#--------------------------------------------------------------------#         
    # Instantiating objects from csv file:
    # How this method is going to instance, it can't be acess by the instance
    # It can only be access from the class level, and it's why we call it by Class method
    @classmethod # --> decorators changed the behavior the function we are calling.
    def instantiate_from_csv(cls) -> None:
        with open("04 - Class vs Static Methods/codesnippets/items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        # Instantiating the objects:
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
#--------------------------------------------------------------------#         
          
    # Static methods has some logical conection to an class
    # Like check if an value is an int or a float...
    @staticmethod # like isolated functions
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0 ...
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
            
#--------------------------------------------------------------------#       
    # Imprimir itens:
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"
#--------------------------------------------------------------------#

print(Item.is_integer(7))

# Item.instantiate_from_csv()
# print(Item.all)