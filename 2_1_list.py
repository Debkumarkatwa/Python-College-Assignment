lst=[]

while  True:
    element=input(f"Enter the {size+1} element: ")
    if element!= 'q':
        lst.append((element))
    else:
        print("The Elements of the List are:: ")
        print(lst)
        break
