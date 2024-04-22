def power(n,p):
    if p!=1:
        return n*power(n,p-1)
    else:
        return n
    

print(power(5,3))