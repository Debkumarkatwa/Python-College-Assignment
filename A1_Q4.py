#Calculate and print the factorial of n using Python.

n=int(input("Enter the Number:: "))
result=1
for i in range(n,0,-1):
    print(i)   
    result=result*i
print(f"The factorial of {num} is {result}")