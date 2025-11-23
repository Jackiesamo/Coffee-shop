class Order:
    #class variable to store all orders
    orders = []

    def __init__(self,customer,coffee,price):
     self.customer =customer
     self.coffee =coffee
     self.price =price

     #add this order to the list of orders
     Order.orders.append(self)

     @property
     def customer(self):
        return self ._customer
     
     @customer .setter
     def customer(self,value):
        self ._customer = value
        if not isinstance(value,customer):
           print('customer must be an instance of customer class')
        self ._customer = value

        @property
        def coffee(self):
          return self ._coffee
     
     @coffee .setter
     def coffee(self,value):
        self ._coffee = value
        if not isinstance(value,coffee):
           print('coffee must be an instance of coffee class')
        self ._coffee = value

        @property
        def price(self):
          return self ._price
     
     @price .setter
     def price(self,value):
        self ._price = value
        if not isinstance(value,float):
           print('price must be a float')
        if not(1.0<=value<=10.0):
           raise TypeError('price must be between 1.0 and 10.0')
        self ._customer = value






           


    