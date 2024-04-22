import random as rd
finalscore=0
while True:
    attem=5
    print("\n\n\nWelcome to the game")
    print("You have 5 attempt to guess the number")
    marks=0
    x=rd.randint(1,20)
    for i in range(0,5):
        y=int(input("\nGuess the number between 1-20: "))
        attem-=1
        if y==x:
            print("You guessed is right")
            if attem==4:
                marks+=5
            elif attem==3:
                marks+=4
            elif attem==2:
                marks+=3
            elif attem==1:
                marks+=2
            elif attem==0:
                marks+=1
            print("Your score is ",marks)
            break

        elif y>x:
            print("Sorry!! you are wrong")
            print(f"CHOOSE a smaller number......\t you had {attem} attempt left")
        elif y<x:
            print("Sorry!! you are wrong")
            print(f"CHOOSE a larger number......\t you had {attem} attempt left")
    else:
        print("Sorry!! You are out of Chance....\nThe correct num is ",x)
        print("\n............Your total score is ",finalscore)
        break
    
    finalscore+=marks
    print("\n............Your total score is ",finalscore)
        
