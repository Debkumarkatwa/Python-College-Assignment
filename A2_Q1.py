lst=[]
size=int(input("Enter the size of the list:: "))

for i in range(size):
    element=input(f"Enter the {i+1} element: ")
    lst.append(element)


print("The Elements of the List are:: ")
for i in range(size):
    print(lst[i],end=", ")
print()
