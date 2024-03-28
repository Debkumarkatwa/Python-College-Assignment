#integers=[]
odd=[]
even=[]
i=0

while True :
    element=input(f"Enter the {i+1} integer: ")
    if element=='q':
        break
    a=int(element)
    if a%2 == 0:
        even.append(a)

    else :
        odd.append(a)
    
    i+=1
    #integers.append(element)


print("The EVEN Elements of the List are:: ")
print(even)

print("The ODD Elements of the List are:: ")
print(odd)

