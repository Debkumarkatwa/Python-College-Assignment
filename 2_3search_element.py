lst=[]
size=int(input("Enter the size of the list:: "))

for i in range(size):
    element=input(f"Enter the {i+1} element: ")
    lst.append(element)


print("The Elements of the List are:: ")
for i in range(size):
    print(lst[i],end=", ")
print()

find=input("Enter the element you want to find: ")

'''
Finding an element without using a loop-----
if find in lst:
    print(found)
else:
    print(not found)
'''

for i in range(size):
    if find==lst[i]:
        print(f"The element was founded in index {i}")
        break

else :
    print("SORRY!! The element is not in the list........")

