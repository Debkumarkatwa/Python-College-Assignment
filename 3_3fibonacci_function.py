a,b=0,1
lst=[0,]
def fibonacci():
    x=1
    while x!=0:
        x=int(input("Enter '0'for break:: "))
        global a,b
        lst.append(b)
        a,b=b,a+b
        print(f"\nThe Fibonacci Series is{lst}\n")

fibonacci()