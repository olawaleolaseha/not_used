# x = 0
# while x <= 10:
#     print(x)
#     x += 2

# data = [1,2,3,4,5,6,7,8,9,10]
# print(6 in data) # this is like saying "Is 6 in data?" Since the answer is YES, it will return True. The print in front is just for me to confirm what i think is correct

#always note that input converts your format to string by default (even if user enter a number). If you want to ensure the value you want to to take from input
#  is a number, use "int" or "float" on it as the case may be.
#e.g
#test = int(input("enter your age: ")) # first gets the input from user, then turns to integer before storing in "test" variable
#print(test) 

# x = int(input("enter x: "))
# y = int(input("enter y: "))
# def aropo(x,y):
#     print(x+y)

# aropo(7,10)
# aropo(x,y)
#we can always call the function "aropo" whenever we need it instead of always writing a code to add two numbers.

# data = [1,2,3,4,5,6,7,8,9,10]
# for i in data:
#     if i % 2 == 0:
#         print(i)

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input("enter a word in lower case to check if palindrum: ")
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")
   
