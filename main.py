# from item import Item 
from phone import Phone 
from keyboard import Keyboard


# Item.instantiate_from_csv()#------------------
# item1 = Item("MyItem", 750) 
#setting an attribute 
# item1.name = "OtherItem" 

#READ ONLY
#will not update unless we give _name. To make it read-only, give double underscore
#double underscore prevents access of those attributes from outside the class 
#we can't access it from double underscore now. Will have to read it as a property now only

#We can again set a different value by using setters through @name.setter 
# print(item1.__name)
# print(item1.price)
#---------------------------Lab 2 


#inheritance : child class phone
    
# Item.instantiate_from_csv()
# print(Item.is_integer(7.09))
    

#we create a spearate class that stores the fucntionalities that item class brings with it. We cannot store them in the
#same class as the previous one as it might not be useful for other itmes we create. It might be useful for phone but not for other items. 
#we create a new class phone which will inherit all the properties of class also 
#there are child classes and parent classes. 
 

#--------------------------------encapsulation
# It describes the idea of wrapping data and the methods that work on
# data within one unit. This puts restrictions on accessing variables
# and methods directly and can prevent the accidental modification of data.
# To prevent accidental change, an object’s variable can only be changed by
# an object’s method. Those types of variables are known as private variables.

# item1 = Item("MyItem", 750)
# item1.apply_increment(0.2)
# item1.apply_discount()
# print(item1.price)

#--------------------------------abstration
# Data abstraction is one of the most essential concepts of Python OOPs which 
# is used to hide irrelevant details from the user and show the details that 
# are relevant to the users.

# Data abstraction in Python is a programming concept that hides complex 
# implementation details while exposing only essential information and
#  functionalities to users. In Python, we can achieve data abstraction
#  by using abstract classes and abstract classes can be created using
#  abc (abstract base class) module and abstractmethod of abc module.
#In other languages, there are public and private variables which do the same.
#abstract the informatin that is unecessary from your instances 


# item1 = Item("MyItem", 750, 6)

# item1.send_email()

#________________________________________________________

#INHERITANCE 
# It allow us to reuse our code across our classes. We have created many classes here which are child 
# classes of the item class. Each child class represents a type of item. 

# item1 = Phone("jscPhone", 1000, 3)
# item1.apply_increment(0.2)
# item1.apply_discount()                #we can use it on the phone class even when it was never implemented in it due to polymorphism 

# print(item1.price)


#------------------------------------------------------------------
#POLYMORPHISM
#we can use apply_discount on several classes 

item1 = Keyboard("jscKeyboard", 1000, 3)

#we have fixed a different pay_rate for keyboard but the method is the same 
item1.apply_discount()

print(item1.price)
