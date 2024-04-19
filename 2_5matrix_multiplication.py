matrix1=[]
matrix2=[]
m=[]
r1=int(input("Enter the number of rows of 1st matrix:"))
c1=int(input("Enter the number of columns of 1st matrix:"))
r2=int(input("Enter the number of rows of 2nd matrix:"))
c2=int(input("Enter the number of columns of 2nd matrix:"))
if r1!=c2:
    print("Matrix multiplication is not possible")
else:
    for i in range(c1):
        for j in range(r1):
            m.append(input(f"Enter the {i}{j} element of 1st matrix:"))
        matrix1.append(list(m))
        m.clear()
    for i in range(c1):
        for j in range(r1):
            m.append(input(f"Enter the {i}{j} element of 1st matrix:"))
        matrix1.append(list(m))
        m.clear()

print("1st matrix is")
for i in range(c1):
    print(matrix1[i])
    
print("2nd matrix is")
for i in range(c2):
    print(matrix2[i])



result=[]

# for i in range(c1):
#     for j in range(r2):
#         for k in range(c1):
#             m.append(matrix1[i][k])*(matrix2[k][j])
#         result.append(sum(m))
#         m=[]

# print(result)
    
