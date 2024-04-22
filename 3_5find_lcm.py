def Lcm(x,y):
    larger = max(x, y)
    for i in range(larger, x * y + 1):
        if i % x == 0 and i % y == 0:
            return i
        
def Gcd(x, y):
    smallar = min(x, y)
    for i in range(smallar, 0, -1):
        if x % i == 0 and y % i == 0:
            return i
    

while True:
    result =int(input("Enter 1 to find GCD and 2 to find LCM & 0 for exit: "))
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if result == 1:
        result = Gcd(num1, num2)
        print(f"The GCD of {num1} and {num2} is {result}")
    elif result == 2:
        result = Lcm(num1, num2)
        print(f"The LCM of {num1} and {num2} is {result}")
    elif result == 0:
        break
    else:
        print("Invalid input. Please enter 1 or 2.")
