#--------------------------------------------------------------------#
# Sixth program: Getters & Setters
# Created by: Jim - https://www.youtube.com/watch?v=lmAc1_R4Z0Q
# Changed by: Thiago Piovesan
# Objective: Learning about getter and setter methods.
#--------------------------------------------------------------------#

# Libs importations
from item import Item
#--------------------------------------------------------------------#

# We create a new object, because we'll have some exclusive attributes
item1 = Item("MyItem", 750)

# This new attribute does not exist, so we are going to create it using...
# Setting an Attribute
item1.name = "OtherItem"

# Getting an Attribute
print(item1.name)
#--------------------------------------------------------------------#