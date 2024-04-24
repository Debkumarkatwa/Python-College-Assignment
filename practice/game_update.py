import random as rd
finalscore=0
num,round,track,attem,ma=20,1,20,5,5
while True:
    print("\n\n\nWelcome to the game")
    print(f"This is round {round}")
    print(f"You have {attem} attempt to guess the number")
    marks=0
    x=rd.randint(1,num)
    for i in range(0,attem):
        y=int(input(f"\nGuess the number between 1-{num}: "))
        attem-=1
        if y==x:
            print("You guessed the right number")
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
            print(f"Choose a SMALLER number......\t you had {attem} attempt left")
        elif y<x:
            print("Sorry!! you are wrong")
            print(f"Choose a LARGER number......\t you had {attem} attempt left")
    else:
        print("Sorry!! You are out of Chance....\nThe correct num is ",x)
        print("\n............Your total score is ",finalscore)
        break
    
    finalscore+=marks
    print("\n............Your total score is ",finalscore)
    num+=5
    round+=1
    attem=ma
    if (num-track)>=20:
        ma+=1
        track+=20
    if num>100:
        print("You have reached the maximum limit of the game")
        break
