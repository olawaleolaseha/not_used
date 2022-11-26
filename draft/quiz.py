print("Test your knowledge!")

wanaplayornot = input("Are you ready to show off how much you know? Yes/No: ")

if wanaplayornot.lower() != "yes":
    print ("Sure, we can do this when next you are in the mood! Heheheh")
    quit()

print("Great! Let's start! :)")
testtaker = input ("But before we start, please enter your name here: ")
score = 0

answer = input("What is Dapo's favorite toy? ")
if answer.lower() == "mario":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What are the last 2 syllables of mummy's first name? ")
if answer.lower() == "wumi":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What are the last 2 syllables of daddy's first name? ")
if answer.lower() == "wale":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is your brother's name (last 2 syllables)? ")
if answer.lower() == "mide":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What is Dapo's date of birth (MMDDYYYY)? ")
if int(answer) == 12022014:
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What is daddy's best food (it starts with 'a' and ends with 'a'? ")
if answer.lower() == "amala":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print (testtaker, "got " + str(score) + " questions correct!")
print (testtaker, "got " + str((score / 6) * 100) + "%.")

if score < 4: #pass mark is 4 of 6
    print ("uh-oh, do you want to try again?")
else:
    print ("great job", testtaker,"!")
