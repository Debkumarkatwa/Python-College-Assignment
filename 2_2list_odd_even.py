#integers=[]
odd=[]
even=[]
e,o=0,0
size=int(input("Enter the size of the list:: "))

for i in range(size):
    element=int(input(f"Enter the {i+1} integer: "))
    if element%2 == 0:
        even.append(element)
        e=e+1

    else :
        odd.append(element)
        o=o+1

    #integers.append(element)


print("The EVEN Elements of the List are:: ")
for i in range(e):
    print(even[i],end=", ")
print()

print("The ODD Elements of the List are:: ")
for i in range(o):
    print(odd[i],end=", ")

