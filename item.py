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
        self.__name = name            #name is read-only so we need to give two underscore before it to set it read only
        self.__price = price

        self.quantity = quantity 

        Item.all.append(self) 

    @property 
    def price(self):
        return self.__price 

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate 

    

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value        

    def __price(self, price):
        self.price = price

    def new_method(self, price):
        self.price = price  

    @property
    #Property decorator = read-only attribute
    def name(self):
        return self.__name  

    #to set a value in name even when it is already made read-only
    @name.setter
    def name(self, value):
        if len(value)>10 :
            raise Exception("The name is too long!")       #we can also execute other lines of code here 
        self.__name = value

    



    def calculate_total_price(self):
        return self.price*self.quantity
    
    # def apply_discount(self):
    #     self.price = self.price * self.pay_rate

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
    
    #for email:
    def __connect(self, smtp_server):    
       pass 

    #prepare body for formatted mail 
    #we added double underscore means that these methods can only be accessed
    #from inside the class, user cannot directly access it : data abstraction
    def __prepare_body(self):
       return f"""
       Hello Someone.
       We have {self.name} {self.quantity} times.
       Regard, Riyaa
       """
    
    def __send(self):
        pass
   
    #pass the required methos for calling emails inside send email method 
    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
        



    

    # #creating read-only attribute: user cannot change the value once set 
    # @property
    # def read_only_name(self):
    #     return "AAA"
