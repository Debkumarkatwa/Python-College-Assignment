lst=[]

while(True) :
    print("****************MENU****************")
    print("1=Display")
    print("2=Search")
    print("3=Insert")
    print("4=Delete")
    print("5=Count")
    print("6=Exit")
    print("====================================")

    choice=int(input("What Are you want to Do:: "))
    
    if choice==1 :
        for i in lst :
            print(i,end=", ")
        print()
    
    elif choice==2 :
        find=input("Enter the element you want to find: ")

        for i in range(size):
            if find==lst[i]:
                print(f"The element was founded in index {i}")
                break
        else :
            print("SORRY!! The element is not in the list........")

    elif choice==3 :
        element=input("Enter the new element: ")

        lst.extend(element)
        
    elif choice==4 :
        index=int(input("Which Index's element are you want to delete:: "))
        
        lst.pop(index)
 
    elif choice==5 :
        print(f"The lenth of the list is {len(lst)}")
        
    elif choice==6 :
        break
    
    else :
        print("Invalid Choice")
