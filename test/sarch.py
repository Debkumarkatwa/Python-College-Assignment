lst=[]
i=0
while  True:
    element=input(f"Enter the {i+1} element: ")
    if element!= 'q':
        lst.append(int(element))
        i+=1
    else:
        break

print("The Elements of the List are:: ")
for i in lst:
    print(i,end=", ")
print()

find=input("Enter the element you want to find: ")

if find in lst:
    print("found")
else:
    print("not found")

