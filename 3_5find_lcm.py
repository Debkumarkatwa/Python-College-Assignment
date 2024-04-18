def fun(x,y):
    larger = max(x, y)
    for i in range(larger, x * y + 1):
        if i % x == 0 and i % y == 0:
            return i

while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = fun(num1, num2)
    print(f"The LCM of {num1} and {num2} is {result}")
