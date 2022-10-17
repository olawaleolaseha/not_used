# instantiating from a csv file (in this case , from the file items.csv). We want our list of items to be in a csv...we can maintain the items from there...

import csv
class Item: #Item is the class.
     
    pay_rate = 0.8 #price after applying 20% discount). Compare with line 32 for illustration purpose.
    all = []
    def __init__(self, name: str, price: float, qty: float):

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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                qty = int(item.get('qty')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    def __repr__(self): # magic method to help us display the items in a list. It works with line 54
        return f"Item('{self.name}', '{self.price}', '{self.qty}')"

# item1 = Item("Phone", 2000, 9)
# item2 = Item("Laptop", 3000, 5)
# item3 = Item("Mouse", 100, 6)
# item4 = Item("Cable", 50, 7)
# item5 = Item("Keyboard", 70, 11)
# etc...refer to the connected csv file (items.csv) for more items.

Item.instantiate_from_csv()
print(Item.all) # confirms items.csv file contains our objects in csv format and can be maintained from there

# What is the difference between @classmethod and @staticmethod? classmethod is used to instantiate from a structured data file like CSV. static method is with a parameter (not a whole class)
# to help return an integer data type despite the data haveing .0 at the end.