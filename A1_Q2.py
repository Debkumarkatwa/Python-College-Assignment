#menu={
#    1 : "Addition",
#    2 : "Subtraction",
#    3 : "Multiplication",
#    4 : "Division",
#    5 : "Reminder",
#    6 : "Quotient",
#    7 : "Exponent"
#}
#for i in menu:
#    print(i,menu[i])
print(" 1 : Addition,\n 2 : Subtraction,\n 3 : Multiplication,\n 4 : Division,\n 5 : Reminder,\n 6 : Quotient,\n 7 : Exponent")
ch=int(input("Enter Your Choice: "))
if ch>7 or ch<1:
    print("SORRY:: You enter a wrong Oparator")
else :
    a=int(input("Enter Number1: "))
    b=int(input("Enter Number2: "))
    if ch==1:
        r1=a+b
        print(f"Sum of {a} and {b} is {r1}")
    elif ch==2:
        r1=a-b
        print(f"Subtraction of {a} and {b} is {r1}")
    elif ch==3:
        r1=a*b
        print(f"Multiplication of {a} and {b} is {r1}")
    elif ch==4:
        r1=a/b
        print(f"Division of {a} and {b} is {r1}")
    elif ch==5:
        r1=a%b
        print(f"Reminder of {a} and {b} is {r1}")
    elif ch==6:
        r1=a//b
        print(f"Quotient of {a} and {b} is {r1}")
    elif ch==7:
        r1=a**b
        print(f"Exponent of {a} and {b} is {r1}")
print("Thank you for using it \nit is created by Deb kumar ")
