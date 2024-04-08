lst=[]
while True:
    ele=(input("Enter the elements:: "))
    if ele=='q' :
        break
    else:
        lst.append(ele)

print("List is ",lst)

#append
#extend
#insert
#pop
#remove
#del
#reverse
#copy


#len()
print(f"lenth of the List is {len(lst)}")

#index()
var=input("what are you want to find:: ")
print(f"the index of {var} is {lst.index(var)}")

#min() and max()
print(f"The minimum value in the List is {min(lst)}")
print(f"The maximum value in the List is {max(lst)}")

#sorted() and sort()
f=(sorted(lst))
print(f"\nthe sorted List is :{f}")
print("Modified list is :: ")
lst.sort()
print(lst)

#count()
var=input("what are you want to count:: ")
print(f"{var} appears {lst.count(var)} times in the List")
