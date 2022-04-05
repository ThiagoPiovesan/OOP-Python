#--------------------------------------------------------------------#
# Seventh program: OOP Principles Explained with Examples
# Created by: Jim - https://youtu.be/ZVTuWsrjvyU
# Changed by: Thiago Piovesan
# Objective: Learning about Encapsulation, Abstraction, Inheritance and Polymorphism.
#--------------------------------------------------------------------#

# Libs importations
from item import Item

# We create a new object, because we'll have some exclusive attributes
# So, we can create a inheritance from the Item class
class Phone(Item):              # Child class
    pay_rate = 0.5
    
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        # Allow us to only create the child attributes / methods
        super().__init__(
            name, price, quantity
        )
    #--------------------------------------------------------------------#
        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"
    #--------------------------------------------------------------------#
        # Assign to self object
        self.broken_phones = broken_phones
        
#--------------------------------------------------------------------#