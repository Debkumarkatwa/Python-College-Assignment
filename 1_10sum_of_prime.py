#Using a while loop to find and print the sum of all prime numbers less than or equal to n.

num=int(input("Enter a number : "))
i,s=2,0
while i<=num:
    f=0
    for j in range(2,i):
        if i%j==0:
            f=1
            break
    if(f==0):
        s=s+i
        print(i,end=" ")
    i=i+1
print("\nThe sum of prime number is : ",s)

