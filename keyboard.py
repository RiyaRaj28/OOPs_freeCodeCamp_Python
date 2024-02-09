from item import Item

class Keyboard(Item):
        pay_rate = 0.7         #overwriting in child class is allowed 
        
        def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
          #call to super function to have access to all attrobutes and methonds
          super().__init__(name, price, quantity)


