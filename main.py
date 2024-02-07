import csv 

class Item :
    #defining class attribute 
    pay_rate = 0.8 
    all = []
    def __init__(self, name:str, price:float, quantity=0):

        #run validations to check price, quantity
        assert price>=0, f"Entered price {price} is not greater than or equal to 0!"
        assert quantity>=0, f"Entered quantity {quantity} is not greater than or equal to 0!"

        #assign attributes to self object 
        self.name = name
        self. price = price
        self.quantity = quantity 

        Item.all.append(self)   

    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open(r'C:\Users\rrajj\OneDrive\Desktop\Python\OOPs_freeCodeCamp\items.csv', 'r') as f :
            reader = csv.DictReader(f)
            items = list(reader)    

        for item in items :
            print(item)

    #static methods 
    @staticmethod
    def is_integer(num):
        #don't count floats that have point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True 
        else:
            return False  

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"   #{self.__class__.name__}: is used to access the name of the class




#inheritance : child class phone
    
class Phone(Item):
        
        def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
          #call to super function to have access to all attrobutes and methonds
          super().__init__(name, price, quantity)

        #run validations to check price, quantity
          assert broken_phones>=0, f"Broken phones {broken_phones} is not greater than or equal to 0!"

        #assign attributes to self object 
          self.broken_phones = broken_phones 

 





# Item.instantiate_from_csv()
# print(Item.is_integer(7.09))
    

#we create a spearate class that stores the fucntionalities that item class brings with it. We cannot store them in the
#same class as the previous one as it might not be useful for other itmes we create. It might be useful for phone but not for other items. 
#we create a new class phone which will inherit all the properties of class also 
#there are child classes and parent classes. 


phone1 = Phone("phone10", 500, 5, 1)

#by using the super function we call this attribute of phone into class also 
print(Item.all)
print(Phone.all)



 