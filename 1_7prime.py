#Check If the number is positive, check if it is a prime number.

num=int(input("Enter the number you want to check:: "))
check=0

if num==0 :
    print("SORRY!! The number is ZERO(0) ")

elif num<0 :
    print(f"SORRY!! The number({num}) is a NEGATIVE(-) Number")

else :
    print(f"The number({num}) is a POSITIVE(+) Number")
    f=0
    for j in range(2,num):
        if num%j==0:
            f=1
            break
    if(f==0):
        print(num,"is a prime number")
    else:
        print("Sorry!!",num,"is NOT a prime num")

        
