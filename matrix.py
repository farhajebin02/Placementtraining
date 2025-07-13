x,y=map(int,input().split())
matrix1=[]
for i in range(x):
    row=list(map(int,input().split()))
    matrix1.append(row)
matrix2=[]    
for i in range(x):
    row=list(map(int,input().split()))
    matrix2.append(row)   
sum=[]
for i in range(x):
    row=[]
    for j in range(y):
        row.append(matrix1[i][j]+matrix2[i][j])
    sum.append(row)    
print("First Matrix:")
for row in matrix1:
    print(*row)
print("Second Matrix:")
for row in matrix2:
    print(*row)
print("Sum of the two matrices is:")
for row in sum:
    print(*row)
