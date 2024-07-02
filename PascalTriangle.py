n=int(input())
table=[[0 for i in range(n+1)] for j in range(n+1)]
for row in range(0,n+1):
    for col in range(row):
        print(table[row][col],end=" ")
    print()
print("===================")
table[0][0]=1
table[1][0]=1
table[1][1]=1

for row in range(2,n+1):
    for col in range(row+1):
        if col==0 or col==row-1:
            table[row][col]=1
        else:
            table[row][col]=table[row-1][col-1]+table[row-1][col]
print("Pascal Triangle")
for row in range(0,n+1):
    for col in range(row):
        print(table[row][col],end=" ")
    print()
