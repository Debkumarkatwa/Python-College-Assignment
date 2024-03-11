#Implement a while loop to repeatedly ask the user for a number until they enter a negative number. For each entered positive number, calculate and print its factorial.

i,num,result=0,0,1
while num >=0 :

    num=int(input("Enter the Number you want:: "))
    if num<0 :
        print("\n SORRY!! This is a negative value")
        print("Thanks for using!!")
    else :
        for i in range(num,0,-1):   
            result=result*i
        print(f"The factorial of {num} is {result}")
        result=1
