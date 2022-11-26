name = input("What is your name? ")
print("Hello,", name)
input("how are you?")
print("good to know")
age = int(input("how old are you?"))
print("really, you are", age, "?", "you are too old oh")

# I wrote the lines below to test if the tabnine i just installed is working.
#always note that input converts your format to string by default (even if user enter a number). If you want to ensure the value you want to to take from input
#  is a number, use "int" or "float" on it as the case may be.
y = float(input("enter your height in feet: "))
x = input("enter your complexion: ")
print("good to know that you are now",y, "feet tall", "and you are", x, "in complexion")
print(f"good to know that you are now {y} feet tall and you are {x} in complexion") #f here is format. It helps format the statement. This is my preferred output formatting
print("good to know that you are now" ,y, "feet tall" + "and you are" +  x  +  "in complexion")# This is not good as it will join 
#tall&add together even if you put spaces around the +. same thing around dark. I think this is how concatenation works...investigate later
print("good to know that you are now {} feet tall and you are {} in complexion" .format(y,x))
print("good to know that you are now %d feet tall and you are %s in complexion" %(y,x))




