import random as rd

print("Welcome to the game")
print("You have to choose between rock, paper and seasor")
print("Enter 'q' to quit the game")

score,game=0,0

while True:
    com=rd.choice(["rock","paper","seasor"]) #computer's choice
    user=input("Enter your choice: ").lower()   
    if user=="q":
        break

    if user==com:
        print("It's a tie")
        game-=1

    elif user=="rock":
        if com=="paper":
            print("You lose")
        else:
            print("You win")
            score+=1

    elif user=="paper":
        if com=="seasor":
            print("You lose")
        else:
            print("You win")
            score+=1

    elif user=="seasor":
        if com=="rock":
            print("You lose")
        else:
            print("You win")
            score+=1

    else:
        print("Invalid choice")
        continue

    print(f"Computer's choice is {com}")       
    game+=1
    
print("Thanks for playing the game")
print(f"Your score is {score} out of {game}")

