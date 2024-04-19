def check_prime(num):
    f=0
    for j in range(2,num):
        if num%j==0:
            f=1
            break
    if(f==0):
        print(num,"is a prime number")
    else:
        print("Sorry!!",num,"is NOT a prime num")

num=int(input("enter the number:"))
check_prime(num)