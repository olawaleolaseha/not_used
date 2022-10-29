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

# def isPalindrome(s):
#     return s == s[::-1]
 
 
# Driver code
# s = input("enter a word in lower case to check if palindrum: ")
# ans = isPalindrome(s)
 
# if ans:
#     print("Yes")
# else:
#     print("No")
   
# cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
# capitalized_cities = []

# for city in cities:
#     capitalized_cities.append(city.title())

# # print(cities)
# book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
# word_counter = {}

# # for word in book_title:
# #     if word not in word_counter:
# #         word_counter[word] = 1
# #     else:
# #         word_counter[word] += 1
# # print(word_counter)

# for word in book_title:
#     word_counter[word] = word_counter.get(word, 0) + 1
# print(word_counter)
# book_title_caps = []
# for i in book_title:
#     i = i.upper()
#     book_title_caps.append(i)

# print(book_title_caps)
# print(book_title)

# cast = {
#            "Jerry Seinfeld": "Jerry Seinfeld",
#            "Julia Louis-Dreyfus": "Elaine Benes",
#            "Jason Alexander": "George Costanza",
#            "Michael Richards": "Cosmo Kramer"
#        }
# for k,v in cast.items():
#     #print(k,v)
#     print(f"actor {k} bears {v} in movies")

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# # fruits.  Use the dictionary and list to count the total number
# # of fruits, but you do not want to count the other items in your basket.

# result = 0
# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# #Iterate through the dictionary

# #if the key is in the list of fruits, add the value (number of fruits) to result
# for k,v in basket_items.items():
#     if k in fruits:
#         result = result + v
    

# print(result)


# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.


# fruit_count, not_fruit_count = 0, 0
# basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
# fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# #Iterate through the dictionary

# #if the key is in the list of fruits, add to fruit_count.
# for k,v in basket_items.items():
#     if k in fruits:
#         fruit_count = fruit_count + v
#     else:
#         not_fruit_count = not_fruit_count + v
# #if the key is not in the list, then add to the not_fruit_count


# print(fruit_count, not_fruit_count)

# card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
# hand = []

# # adds the last element of the card_deck list to the hand list
# # until the values in hand add up to 17 or more
# while sum(hand)  < 17:
#     hand.append(card_deck.pop())
# print(hand)


# num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

# odd_num_list = []
# for i in num_list:
#     if i % 2 == 1:
#         odd_num_list.append(i)
# print(odd_num_list)

# print(odd_num_list[0:4])

# sum_1st_5 = 0
# for j in odd_num_list[0:5]:
#     sum_1st_5 += j

# print(sum_1st_5)

# egg_count = 0

# def buy_eggs():
#     egg_count += 12 # purchase a dozen eggs

# buy_eggs()

# how_many_snakes = 1
# snake_string = """
# Welcome to Python3!

#              ____
#             / . .\\
#             \  ---<
#              \  /
#    __________/ /
# -=:___________/

# <3, Juno
# """


# print(snake_string * how_many_snakes)

#==============================================================================================
# Handling Errors

# def party_planner(cookies, people):
#     leftovers = None # when I commented out lines 176 and 177, the program crashed on line 186. Try again later when you understand more! Figure out the importance of these 2 lines.
#     num_each = None
#     # TODO: Add a try-except block here to
#     #       make sure no ZeroDivisionError occurs.
#     try:
#         num_each = cookies // people
#         leftovers = cookies % people
#     except ZeroDivisionError:
#         print("We need to have at least one person in the party")

#     return(num_each, leftovers)

# # The main code block is below; do not edit this
# lets_party = 'y'
# while lets_party == 'y':

#     cookies = int(input("How many cookies are you baking? "))
#     people = int(input("How many people are attending? "))

#     num_each, leftovers = party_planner(cookies, people)

#     if num_each:  # if cookies_each is not None
#         message = f"\nLet's party! We'll have {people} people attending, they'll each get to eat {num_each} cookies, and we'll have {leftovers} left over."
#         print(message)

#     lets_party = input("\nWould you like to party more? (y or n) ")

#================================================================================================================

# # testing math library
# import math

# x = float(input("enter a number with decimal points: "))

# print(math.ceil(x))

#==================================================================================================================
# line = 'Wale Olaseha'

# letter = line[0]

# print(letter)

#========================================================================================================================

#Quiz Game:
print("\nWelcome to this short quiz game!\n")
checker = input("Would you like to play today? Yes/No: ")
if checker.lower() == 'yes':
    print("\nGreat, let's do this\n")
else:
    print("See you some other times, then")
    quit()

corr_ans = 0
ques_no = 0

ques = print("Q1: What is the capital of Alberta? :\nA. Calgary\nB. London\nC. Edmonton\nD. Nunavut")
ans = input("enter your answer here: ")
ques_no += 1
if ans.lower() == 'c':
    corr_ans += 1

ques = print("\nQ2: What is the capital of Ondo? :\nA. Oyo\nB. London\nC. Nunavut\nD. Akure")
ans = input("enter your answer here: ")
ques_no += 1
if ans.lower() == 'd':
    corr_ans += 1

ques = print("\nQ3: What is the capital of Ontario? :\nA. Toronto\nB. London\nC. Nunavut\nD. Akure")
ans = input("enter your answer here: ")
ques_no += 1
if ans.lower() == 'a':
    corr_ans += 1

ques = print("\nQ4: What is the capital of Texas? :\nA. Toronto\nB. Austin\nC. Nunavut\nD. Akure")
ans = input("enter your answer here: ")
ques_no += 1
if ans.lower() == 'b':
    corr_ans += 1

percent_score = (corr_ans / ques_no) * 100
print(f"\nyou got {corr_ans} correctly, so your score is {percent_score}%")

#================================================================================================================================================================
