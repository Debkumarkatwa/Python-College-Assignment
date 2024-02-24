#Check If the number is positive, check if it is a prime number.

num=int(input("Enter the number you want to check:: "))
check=0

if num==0 :
    print("SORRY!! The number is ZERO(0) ")

elif num<0 :
    print(f"SORRY!! The number({num}) is a NEGATIVE(-) Number")

else :
    print(f"The number({num}) is a POSITIVE(+) Number")
    for i in range(2,num//2):
        if num%i == 0 :
            check=check+1
            break
if check==1 :
    print(f"\n BUT!! The number({num}) is NOT a PRIME Number.............")
else :
    print(f"\n\nThe number({num}) is a PRIME Number")
        
