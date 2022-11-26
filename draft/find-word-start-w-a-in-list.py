#Code to print any word that starts with an 'a' oe 'A' from a list of words

fruits = ["apple", "banana", "pineapple", "orange", "Avocado"]
for fruit in fruits:
    if fruit[0].lower() == "a":
        print (fruit)
    else:
        continue