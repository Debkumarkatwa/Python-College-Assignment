import random as rd

print("\n\nWelcome to the game")
print("You have to choose between rock, paper and seasor")
print("Enter 'quit / 0' to exit the game")

score,game=0,0

while True:
    com=rd.choice(["rock","paper","seasor"]) #computer's choice
    user=input("\nEnter your choice:: ").lower()   
    if user=="quit" or user=="0":
        break

    if user==com:
        print("\nIt's a tie")
        game-=1

    elif user=="rock" or "1":
        if com=="paper":
            print("\nYou lose")
        else:
            print("\nYou win")
            score+=1

    elif user=="paper" or "2":
        if com=="seasor":
            print("\nYou lose")
        else:
            print("\nYou win")
            score+=1

    elif user=="seasor" or "3":
        if com=="rock":
            print("\nYou lose")
        else:
            print("\nYou win")
            score+=1

    else:
        print("\nInvalid choice")
        continue

    print(f"Computer's choice is {com}")       
    game+=1
    
print("Thanks for playing the game")
print(f"Your score is {score} out of {game}")

