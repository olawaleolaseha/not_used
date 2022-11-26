# Code modified to have a list of all the item instances that have been created. Lines 5, 16,25,26,38 ___ introduced
class Item: #Item is the class.
     
    pay_rate = 0.8 #price after applying 20% discount). Compare with line 32 for illustration purpose.
    all = [] #
    def __init__(self, name: str, price: float, qty: float): #__init__method is one of many MAGIC METHODS available in python. It is also called Constructor.
                                            #Also note that the args passed in init method could have just been like this " def __init__(self, name, price, qty)". We however
                                            #included the ": str" and ": float" to handle situations where user inputs wrong data types.
        assert price >= 0, f"Price {price} is negative" # used to handle situations where user inputs negative number.
        assert qty >= 0, f"Qty {qty} is negative" # used to handle situations where user inputs negative number.

        self.name = name
        self.price = price
        self.qty = qty

        Item.all.append(self) # code used to append items to the all list on line 3. it has to be created inside the init function.

    def calculate_total_price(self): #name, price, and quantity are the attributes of each object in the class. calculate_total_price is the method.
        return self.price * self.qty

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price
    
    def __repr__(self): # magic method to help us display the items in a list. It works with line 54
        return f"Item('{self.name}', '{self.price}', '{self.qty}')"

item1 = Item("Phone", 2000, 9) #item1 is the first object here. You can now pass the arguments equivalent to the attributes defined in the init of the class
item2 = Item("Laptop", 3000, 5) #item2 is the second object here
item2.pay_rate = 0.7 # discount applies only to second object. Because this line is right below item2 object definition, this takes precedence over the discount defined for the whole class
item3 = Item("Mouse", 100, 6) #item3 is the third object here
item4 = Item("Cable", 50, 7) #item4 is the fourth object here
item5 = Item("Keyboard", 70, 11)

# for instance in Item.all:
#     print(instance.name) # this is a filter function. In this case, it filters out name in the items.

print(Item.all)