def Lcm(a):
    larger = max(a)
    mul=1
    for i in a:
        mul*=i
    for i in range(larger, mul + 1):
        for j in a:
            if i%j!=0:
                break
        else:
            return i
        
def Gcd(a):
    smallar = min(a)
    for i in range(smallar, 0, -1):
        for j in a:
            if j%i!=0:
                break
        else:
            return i
    

while True:
    result =int(input("Enter 1 to find GCD and 2 to find LCM & 0 for exit: "))
    lst=[]
    s=0
    while  True:
        element=input(f"Enter the {s+1} element: ")
        if element!= 'q':
            lst.append(int(element))
            s+=1
        else:
            print("The Numbers are:: ")
            print(lst)
            break
    if result == 1:
        result = Gcd(lst)
        print(f"The GCD of {lst} is {result}")
    elif result == 2:
        result = Lcm(lst)
        print(f"The LCM of {lst} is {result}")
    elif result == 0:
        break
    else:
        print("Invalid input. Please enter 1 or 2.")
