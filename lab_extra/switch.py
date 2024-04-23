x=int(input("fvvgtvtv"))
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
match x:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case 5:
        print(a%b)
    case _:
        print("Invalid input. Please enter 1 or 2.")