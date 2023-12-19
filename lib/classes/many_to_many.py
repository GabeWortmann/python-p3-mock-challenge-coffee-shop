class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self, name):
        if not (type(name) == str):
            print("Exception")
        elif len(name) < 3:
            print("Exception")
        elif hasattr(self, "name"):
            print("Exception")
        else: self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self and isinstance(order, Order)]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum([order.price for order in self.orders()])/self.num_orders()

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self, name):
        if not (type(name) == str):
            print("Exception")
        elif len(name) < 1 or len(name) > 15:
            print("Exception")
        else: self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self and isinstance(order, Order)]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all =[]
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price (self):
        return self._price
    
    @price.setter
    def price (self, price):
        if type(price) != float:
            print("Exception")
        elif price < 1.0 or price > 10.0:
            print("Exception")
        elif hasattr(self, "price"):
            print("Exception")
        else: self._price = price

    @property
    def customer (self):
        return self._customer
    
    @customer.setter
    def customer (self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else: print("Exception")

    @property
    def coffee (self):
        return self._coffee
    
    @coffee.setter
    def coffee (self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else: print("Exception")
