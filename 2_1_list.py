lst=[]
size=0
while  True:
    element=input(f"Enter the {size+1} element: ")
    if element!= 'q':
        lst.append((element))
        size+=1
    else:
        print("The Elements of the List are:: ")
        print(lst)
        break
