n=int(input())
ctr=0
for i in range(4,n+1):
    t=i
    while t>0:
        d=t%10
        if d==4:
            ctr=ctr+1
            break
        t=t//10
print(ctr)
    
