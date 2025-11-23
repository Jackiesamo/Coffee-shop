class Order:
    #class variable to store all orders
    orders = []

    def __init__(self,customer,coffee,price):
     self.customer =customer
     self.coffee =coffee
     self.price =price
     Order.orders.append(self)

     @property
     def customer(self)


    