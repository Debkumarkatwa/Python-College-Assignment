def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multi(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

while True:
    n1=int(input("Enter first number:: "))
    n2=int(input("Enter second number:: "))
    choice=int(input("enter your choice\n1=add\t2=sub\t3=multi\t4=division\n5 for break"))  

    if choice==1:
        print(f"The addition of {n1},{n2} is",add(n1,n2))
    elif choice==2:
        print(f"The subtraction of {n1},{n2} is",sub(n1,n2))
    elif choice==3:
        print(f"The multification of {n1},{n2} is",multi(n1,n2))
    elif choice==4:
        print(f"The division of {n1},{n2} is",div(n1,n2))
    elif choice==5:
        break
    else:
        print("Invalid choice")