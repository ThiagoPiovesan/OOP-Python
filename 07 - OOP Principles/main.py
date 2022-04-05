#--------------------------------------------------------------------#
# Seventh program: OOP Principles Explained with Examples
# Created by: Jim - https://youtu.be/ZVTuWsrjvyU
# Changed by: Thiago Piovesan
# Objective: Learning about Encapsulation, Abstraction, Inheritance and Polymorphism.
#--------------------------------------------------------------------#

# Libs importations
from phone import Phone
from keyboard import Keyboard
#--------------------------------------------------------------------#

item1 = Keyboard("jscKeyboard", 1000, 3)

item1.apply_increment(0.2)
item1.apply_discount()

print(item1.price)

item1.send_email()