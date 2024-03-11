#Check if the number is positive, negative, or zero in python.

num=int(input("Enter the number you want to check:: "))

if num==0 :
    print("The number is ZERO(0) ")

elif num<0 :
    print(f"The number({num}) is a NEGATIVE(-) Number")

else :
    print(f"The number({num}) is a POSITIVE(+) Number")