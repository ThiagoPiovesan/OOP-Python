#--------------------------------------------------------------------#
# Seventh program: OOP Principles Explained with Examples
# Created by: Jim - https://youtu.be/ZVTuWsrjvyU
# Changed by: Thiago Piovesan
# Objective: Learning about Encapsulation, Abstraction, Inheritance and Polymorphism.
#--------------------------------------------------------------------#

# Encapsulation: inibition of access to the attributes of an object
# Abstraction: hiding the details of an object -> only show the essentials
# Inheritance: the ability to create a new class from an existing one -> Reuse code
# Polymorphism: the ability to use the same code for different objects

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
        self.__name = name
        self.__price = price
        self.quantity = quantity
        
        # Actions to execute:
        Item.all.append(self)
#--------------------------------------------------------------------#
    ## Getters and Setters

    ## PRICE ATTRIBUTE    
    # Property Decorator: read-only attribute:
    @property
    def price(self) -> float:
        return self.__price

    # Function to apply discount
    def apply_discount(self) -> None:
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self, increment_value: float) -> None:
        self.__price = self.__price + self.__price * increment_value
#--------------------------------------------------------------------#
    ## NAME ATTRIBUTE
    # Property Decorator: read-only attribute:
    @property
    def name(self):
        print("You are trying to read the name attribute")
        return self.__name
    
    # Allow us to set the name attribute
    # Setter Decorator: write-only attribute:
    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            print("You are trying to set the name attribute")
            self.__name = value
#--------------------------------------------------------------------#                   
    # Function to calculate the total price
    def calculate_total_price(self) -> None:
        return self.__price * self.quantity
        
#--------------------------------------------------------------------#         
    # Instantiating objects from csv file:
    # How this method is going to instance, it can't be acess by the instance
    # It can only be access from the class level, and it's why we call it by Class method
    @classmethod # --> decorators changed the behavior the function we are calling.
    def instantiate_from_csv(cls) -> None:
        with open("/items.csv", 'r') as f:
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
    ## Abstraction concept:
    
    def __connect_to_internet(self, smpt_server) -> None:
        pass
    
    def __prepare_body(self) -> str:
        return f"""
            Hello Sir,
            We have {self.quantity} of {self.name}s in stock.
            Regards,
            Piovesan
        """
    
    # Send email:
    def __send(self) -> None:
        pass
    
    # send email to the user:
    def send_email(self) -> None:
        self.__connect_to_internet("smtp.gmail.com")
        self.__prepare_body()
        self.__send()
#--------------------------------------------------------------------#       
    # Print itens:
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"
#--------------------------------------------------------------------#