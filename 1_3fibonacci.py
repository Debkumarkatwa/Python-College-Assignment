#Generate and print the first n terms of the Fibonacci series using python.

x=int(input("Enter the range:: "))
a,b=0,1
print(f"{a}")
print(f"{b}")
for i in range(x):
    b=a+b
    a=b-a
    print(f"{b}")