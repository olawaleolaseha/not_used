# you remember when you run print(type("wale")) and it gives you <class 'str'>? That shows you Python is OOP language. That is, there is CLASSES and INSTANCES (also called 
# objects). the result <class 'str'> you see shows a class called str has been defined and hardcoded in python base program. Same thing goes for the class 'int'
# too. Infact, same goes for all data types you have seen before starting OOP course.

# Similarly, remember the methods you have used in the past? For example, you used the ".lower()" method to convert upper case strings to lower case strings. This is one
# popular hardocoded method that must have been defined in the default class "str" in python. In OOP too, you will define your custom methods for your custom class. And,
# you will use them same way you use the hardcoded methods...
# By definition, Methods are functions that are inside the classes.
# You will remember that if you have isolated definitions that are not inside a class, those are called Functions. Now you know the difference in the term method and function?

class Item: #Item is the class.
    pay_rate = 0.8 #price after applying 20% discount). Compare with line 32 for illustration purpose.
    def __init__(self, name: str, price: float, qty: float): #__init__method is one of many MAGIC METHODS available in python. It is also called Constructor.
                                            #Also note that the args passed in init method could have just been like this " def __init__(self, name, price, qty)". We however
                                            #included the ": str" and ": float" to handle situations where user inputs wrong data types.
        assert price >= 0, f"Price {price} is negative" # used to handle situations where user inputs negative number.
        assert qty >= 0, f"Qty {qty} is negative" # used to handle situations where user inputs negative number.

        self.name = name
        self.price = price
        self.qty = qty

    def calculate_total_price(self): #name, price, and quantity are the attributes of each object in the class. calculate_total_price is the method.
        return self.price * self.qty

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

item1 = Item("Phone", 2000, 9) #item1 is the first object here. You can now pass the arguments equivalent to the attributes defined in the init of the class
item2 = Item("Laptop", 3000, 5) #item2 is the second object here
item2.pay_rate = 0.7 # discount applies only to second object. Because this line is right below item2 object definition, this takes precedence over the discount defined for the whole class
item3 = Item("Mouse", 100, 6) #item3 is the third object here

#You can now call your method on any of the objects and it will apply the operation you have defined in the class (line 23) on each object. You see how it makes yor code efficient?
#especially if you have a lot of items?

print(item1.calculate_total_price()) # Now it looks like only one line of code can give you the total price of each item. The lines 28 and earlier of the codes are reused.
print(item2.calculate_total_price())
print(item3.calculate_total_price())

#So far we have looked at Instance Atributes (also called object attributes). Now lets look at class attributes: attributes global to the class 
# (i.e always common to all objects in that class).
# Class attribute example is if we are trying to apply a discount of same amount (e.g 20%) across all prices in all instances of a class. We implement this by adding line12
# i.e this attribute is defined at the class level, right below the class declaration line 11. Then we define "apply_discout" method as shown in line 26 to make it global
# to the entire class.

print(item1.apply_discount())
print(item2.apply_discount()) # only this one gets local discount applied. The other items got global discount applied. Refer to line 32 for reason.
print(item3.apply_discount())

# If however, we want a specific discount applied to one item (or one object) in the class, we need to define the discount function right under the object.
# It is important to note that python will first search through the instance to apply the discount before going to the class in this case. It will only apply
# the class-wide discount function if there is none specific or local to the object. E.g we include the lines below 31 above to demonstarte this on item2.