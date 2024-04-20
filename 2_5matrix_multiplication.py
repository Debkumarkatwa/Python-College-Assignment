matrix1=[]
matrix2=[]
m=[]
r1=int(input("Enter the number of rows of 1st matrix:"))
c1=int(input("Enter the number of columns of 1st matrix:"))
r2=int(input("\nEnter the number of rows of 2nd matrix:"))
c2=int(input("Enter the number of columns of 2nd matrix:"))

if c1!=r2:
    print("Matrix multiplication is not possible")

else:
    print("\nEnter elements for matrix1..........")
    for i in range(r1):
        for j in range(c1):
            m.append(int(input(f"Enter the {i+1}{j+1} element of 1st matrix:")))
        matrix1.append(list(m))
        m.clear()
    
    print("\nEnter elements for matrix2..........")
    for i in range(r2):
        for j in range(c2):
            m.append(int(input(f"Enter the {i+1}{j+1} element of 1st matrix:")))
        matrix2.append(list(m))
        m.clear()

    print("\n1st matrix is--------")
    for i in range(c1):
        print(matrix1[i])
        
    print("\n2nd matrix is---------")
    for i in range(c2):
        print(matrix2[i])

    result=[[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    for i in range(c1):
        print(result[i])
        
