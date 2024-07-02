A=list(map(int,input().split()))
B=[]
for i in range(len(A)-1):
    if A[i]>max(A[i+1:]):
        B.append(A[i])
B.append(A[-1])
print(B)

                
