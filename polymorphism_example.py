# POLYMORPHISM

#It refers to the use of a single type entity to represent different types
#in different scenarios ..............poly:many.....morph:forms........
# The ability to have different scenarios when we call the exact same entity(or function)

# used in len built funtion as it can handle different types of objects it receives as an argument 
# and returns result accordingly.
# For example, on using on a string len func returns total number of characters and on applying
# on a list it returns total number of elements inside the list

#Polymorphism can be applied globally 
name = "Jimmy" #str
print(len(name))

some_list = ["some", "name"] #list
print(len(some_list))