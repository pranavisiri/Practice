n=int(input())
for i in range(1,n+1):
    print()
    if i==1:
        for j in range(1,n+1):
            print(j,end=" ")
    if i==n:
        for j in range(n,0,-1):
            print(j,end=" ")
    if i>1 and i<n:
        print(i,end=" ")
        print("- "*(n-2),end="")
        print(n-i+1,end=" ")
