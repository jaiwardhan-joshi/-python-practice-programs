import random
# improvements -1 removed import math 

def guess_game() :
    
     genNumber = random.randint(0,100)
     print("Enter a number between 0-100")
     i = 3
     while True :
        try :
            userNumber = int(input("Enter your number :"))
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
            print("only enter the integers")


            



guess_game()



 