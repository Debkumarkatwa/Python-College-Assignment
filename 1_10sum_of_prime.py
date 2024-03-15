#Using a while loop to find and print the sum of all prime numbers less than or equal to n.

num=int(input("Enter the range you want:: "))
check,j,result=0,2,0

for a in range(2,num+1) :
    result=result+a

while j<=num:
    i=2
    while i*i<=j :
        if j%i==0 :
            result=result-j
        i=i+1
    j=j+1
        
print(f"The Sum of the prime numbers from 0 to ({num}) is a {result}")

num=int(input("Enter a number : "))
i=2
s=0
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

