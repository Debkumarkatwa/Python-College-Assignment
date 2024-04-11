lst=[]

#append
while True:
    ele=(input("Enter the elements('q'for end):: "))
    if ele=='q' :
        break
    else:
        lst.append(ele)
print("List is ",lst)

#extend
c=int(input("want to add more(0/1)"))
if c==1:
    c=input("Enter elements::")
    lst.extend(c)

#insert
c=int(input("want to add somting anywhere(0/1)"))
if c==1:
    c=input("Enter element::")
    p=int(input("Enter position::"))
    lst.insert(p,c)

#pop and remove
c=int(input("want to delete something(0/1)"))
p=int(input("you want to delete by index/value(0/1)::"))
if c==1:
    if p==0:
        c=int(input("Enter the index you want to delete::"))
        lst.pop(c)
    elif p==1:
        c=input("Enter the value you want to delete::")
        if c in lst:
            lst.remove(c)
        else:
            print("it's not in the list")

#reverse and copy
c=int(input("want to reverse the list(0/1)"))
if c==1:
    c=int(input("want to reverse the main list/crate a copy(0/1)"))
    if c==0:
        lst.reverse()
    elif c==1:
        f=lst.copy()
        f.reverse()
        print("the reversed list is",f)

#len()
print(f"lenth of the List is {len(lst)}")

#index()
var=input("what are you want to find:: ")
if var in lst:
    print(f"the index of {var} is {lst.index(var)}")
else:
    print("it's not in the list")

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
