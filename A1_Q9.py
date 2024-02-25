num=int(input("Enter how many coloum you want:: "))

for i in range(1,num+1) :
    for j in range(i) :
        print("*",end="")
    print()

print("\n")

for i in range(1,num+1) :
    for j in range(i) :
        print(j+1,end="")
    print()

print("\n")

for i in range(1,num+1) :
    for j in range(i) :
        print(chr(j+65),end="")
    print()