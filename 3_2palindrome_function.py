def palindrome(num):
    a=str(num)
    a=a[::-1]
    if a==str(num):
        return True
    else:
        return False
    
n=int(input("Enter the number::"))
if palindrome(n):
    print("The number is palindrome")
else:
    print("The number is not palindrome")