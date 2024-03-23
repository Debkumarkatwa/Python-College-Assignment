lst=[]
size=0

while(True) :
    print("****************MENU****************")
    print("1=Display")
    print("2=Search")
    print("3=Insert")
    print("4=Delete")
    print("5=Count")
    print("6=Exit")
    print("====================================")

    choice=input("What Are you want to Do:: ")
    
    if choice=='1' :
        print(lst)
    
    elif choice=='2' :
        find=input("Enter the element you want to find: ")

        for i in range(size):
            if find==lst[i]:
                print(f"The element was founded in index {i}")
                break
        else :
            print("SORRY!! The element is not in the list........")
            while True:
                print("Are you want to add the element in the list?????\nif you want to add press 1 else press 0::")
                ans=int(input())
                if ans ==1:
                    lst.append(find)
                    print("Element added successfully!!!\n\n")
                    break
                elif ans==0:
                    print("Okay!Thanks for using.....")
                    break
                else:
                    print("Invalid input......")
                    print("press a correct input\n\n")

    elif choice=='3' :
        element=input("Enter the new element: ")

        lst.append(element)
        size+=1
        print("Insertion Completed")
        
    elif choice=='4' :
        index=int(input("Which Index's element are you want to delete:: "))
        
        lst.pop(index)
        print("Deletion Completed")

 
    elif choice=='5' :
        print(f"The lenth of the list is {len(lst)}")
        
    elif choice=='6' :
        break
    
    else :
        print("Invalid Choice")
