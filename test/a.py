lst=[]
size=0
while  True:
    element=input(f"Enter the {size+1} element: ")
    if element!= 'q':
        lst.append((element))
        size+=1
    else:
        print("The Elements of the List are:: ")
        for i in range(size):
            print(lst[i],end=", ")
        print()
        break

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
    print("Are you want to add the element in the list?????\nif you want to add press 1 else press 0::")
    ans=int(input())
    if ans ==1:
        lst.append(find)
        print("Element added successfully!!!\n\n")
    elif ans==0:
        print("Okay!Thanks for using.....")
    else:
        print("Invalid input......")

print(lst)

