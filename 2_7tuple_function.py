#tpl=(1,4,2,8,78,52,12,48,75,12,10,88,12)
lst=[]
while True:
    ele=(input("Enter the elements:: "))
    if ele=='q' :
        break
    else:
        lst.append(int(ele))

#tuple
tpl=tuple(lst)
print("Tuple is ",tpl)

#len()
print(f"lenth of the tuple is {len(tpl)}")

#index()
var=int(input("what are you want to find:: "))
print(f"the index of {var} is {tpl.index(var)}")

#min() and max()
print(f"The minimum value in the tuple is {min(tpl)}")
print(f"The maximum value in the tuple is {max(tpl)}")

#sum()
print(f"The sum of all values in the tuple is {sum(tpl)}")

#sorted()
f=(sorted(tpl))
print(f"\nthe sorted tuple is :{f}")

#count()
var=int(input("what are you want to count:: "))
print(f"{var} appears {tpl.count(var)} times in the tuple")
