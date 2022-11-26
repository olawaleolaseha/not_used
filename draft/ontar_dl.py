#pseudocode



# enter your country name in full

# if you user entered nigeria above,

#     print welcome, I will need to ask you a few questions to be able to help you...
#       else, print, sorry, I only have info on Nigerians for now
#

# assign the answer to "which of the ffg documents did you bring from naija A. DL only, B. Abst only, C. Both DL and Abst, D. None." to a Variable
#  if value of variable is A,
#     print (you should go to serviceontario center near you but your chances of being allowed to skip G1 written test is 50-50)
#  elif value of variable is B
#     print (you should get your DL at least before you go to service ontario to apply of ontario DL)
# elif value of variable is C
#     print (Congratulations, you meet the minimum reqmt to be approved to skip the 1 year waiting reqment between ur g1 test and the road test)
# else value of variable is D
#     print (Unfortunately, you will be required to wait for one year after passing your g1 test, before you could take the road test)

# Is there anything else I can help you with today?
# if answer is no, print have a great day.and
# if answer is yes, print Please call Wale on 12345 to program me to be smart enough to help with subjects other than DL guides for Nigerians :)

print("Hello, my name is Lewa and I am happy to guide you on your Drivers License application today")

country = input("Please enter your country in full: ")
country = country.lower()
if country == "nigeria":
    print("\nI have some information for you but I will need to ask you a few questions to be able to help you\n")
else:
    print("\nsorry, I only have info on Nigerians for now")
    exit()

document = input("which of the following documents did you bring from Naija?\n Enter only the corresponding alphabets: \nA. Naija Drivers License, \nB. Naija Drivers Abstract, \nC. Both A&C, \nD. None\n")
document == document.lower()
if document == "a":
    print("you should go to serviceontario center near you but your chances of being allowed to skip G1 written test is 50-50")
elif document == "b":
    print("you should get your Naija DL at least before you go to service ontario to apply of ontario DL")
elif document == "c":
    print("Congratulations, you meet the minimum requirement to be approved to skip the 1 year waiting requirement between ur G1 test and the road test")
else:
    print("Unfortunately, you will be required to wait for one year after passing your g1 test, before you could take the road test")

going_4wd = input("Is there anything else I can help you with today? yes/no: ")
if going_4wd.lower() == "yes":
    print("Please call Wale on 12345 to program me to be smart enough to help with subjects other than DL guides for Nigerians in future.")
else:
    print("have a great day.")