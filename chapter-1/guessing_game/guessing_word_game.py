import random

f = open("words.txt", "r")
words = f.readlines()

i = 0


short_words = []
while i < len(words):
    if len(words[i]) > 2 and len(words[i]) < 5:
        clean_word = words[i].replace("\n", "")
        short_words.append(clean_word)
    i = i + 1

f.close() 

random_pick = random.randint(0, len(short_words) -1 )
def guessing_game() :
    while True:
        user_input = (input("Enter your word! word limit : 2 - 4!")).lower()
        if user_input == short_words[random_pick].lower() :
            print("You got that right!")
            break
        
        elif user_input < short_words[random_pick].lower() :
            print("You choice comes ealier than target word alphabetically!")
        
        elif user_input > short_words[random_pick].lower() : 
            print("Your choice cames later than targer word alphabetically!")

        if len(user_input) < 2 and len(user_input) > 5 :
            print("You're range of input is out of order! please select a word under the range of 2-4!")
        



guessing_game()


    

