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

    choice=input("What Are you want to Do:: ")
    
    if choice=='1' :
        print(lst)
    
    elif choice=='2' :
        find=input("Enter the element you want to find: ")

        if find in lst:
            print(f"The element was founded in index {lst.index(find)}")
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
        element=input("Enter the new element you want to insert:: ")

        lst.append(element)
        print("Insertion Completed")
        
    elif choice=='4' :
        element = input("Enter the element you want to delete: ")
        if element in lst:
            lst.remove(element)
        else:
            print("The element was not found in the list.")

 
    elif choice=='5' :
        print(f"The lenth of the list is {len(lst)}")
        
    elif choice=='6' :
        print("Exiting the program.")
        break
    
    else :
        print("Invalid choice. Please choose a number between 1 and 6.")
