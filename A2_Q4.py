lst=[]
size=int(input("Enter the size of the list:: "))

for i in range(size):
    element=input(f"Enter the {i+1} element: ")
    lst.append(element)


print("The Elements of the List are:: ")
for i in range(size):
    print(lst[i],end=", ")
print()

choice=int(input("Are you want to Delete(0) or Insert(1) the element:: "))

if choice==0 :
    size=size-1
    index=int(input("Which Index's element are you want to delete:: "))
    for i in range(index,size):
        lst[i]=lst[i+1]

elif choice==1 :
    size=size+1
    index=int(input("In Which Index you want to Insert the element:: "))
    element=input("Enter the new element: ")

    for i in range(size-1,index+1):
        lst[i]=lst[i-1]
    lst[index]=element

print("The Elements of the List are:: ")
for i in range(size):
    print(lst[i],end=", ")

