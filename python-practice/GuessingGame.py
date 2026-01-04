import random
# improvements -1 removed import math 

def guess_game() :
    
     genNumber = random.randint(0,100)
     base_number = random.randint(2,16)
     print(f"Guess the number (0 to 100 in decimal), but enter it in base {base_number}")
     i = 3
     while True :
        try :
            userNumber = int(input(f"Enter your number in {base_number} :"), base_number)
            i = i - 1
            if userNumber > genNumber :
                print("Number is too high")
              #improvment -2 removed continue statement (uncesscary)

            elif userNumber < genNumber :
                print("Number is too low")
                

            elif userNumber == genNumber :
                print(f"You are right!")
                break    
            
            if i == 0:
                print("You are out of chances")
                break
            
            print(f"{i} chances left")

        except ValueError :
            print("Invalid number for this base")


            



guess_game()



 