# def mmain():
words = {'Taye': 'Omo akoko', 
            'Kehinde': 'Omo ikeji'
}
while True:
    word_to_check = input("Enter the word you want to check: ")
   
    for k,v in words.items():
        if word_to_check == k:
            print(k, ":", v)
            
    
    if word_to_check == "":
        print('Enter a word pls')
        break
