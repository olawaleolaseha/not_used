quiz = {
    "question1" : {"question" : "1. What is the capital of Canada? :\nA. Alberta B. Toronto C. Montreal D. Ottawa",
    "answer" : "D"
    },
    "question2" : {"question" : "2. What is the capital of Nigeria? :\n",
    "answer" : "Abuja"
    },
    "question3" : {"question" : "3. What is the capital of Ondo? :\n",
    "answer" : "Akure"
    },
    "question4" : {"question" : "4. What is the capital of Lagos? :\n",
    "answer" : "Ikeja"
    },
    "question5" : {"question" : "5. What is the capital of Osun? :\n",
    "answer" : "Osogbo"
    },
}

while True:
    score = 0
    for k,v in quiz.items():
        print(v["question"])
        response = input("Enter your answer: ")
        print("\n")
        if response.lower() == v["answer"].lower():
            score += 1
    print(f"Total score is {score}/{len(quiz)}")
    replay = input("Do you want to replay the quiz? (y/n): ")
    if replay.lower() == "y":
        continue
    else:
        print("Ok, have a nice day and see you some other times")
        break
