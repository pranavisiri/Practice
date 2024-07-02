#optimal solution
nums=int(input("enter no.of values"))
for i in range(nums):
    n=int(input("enter number"))
    nd=0
    t=n
    lst=[]
    while t>0:
        lst.append(t%10)
        t=t//10
        nd=nd+1
    s=0
    for d in lst:
        s+=d**nd
    if s==n:
        print(n," is an armstrong number")
    else:
        print(n," is not an armstrong number")


#general solution      
'''
for i in range(1000,9999):
    count=0
    sum=0
    S=str(i)
    for j in S:
        sum+=int(j)**4
    if sum==i:
        print(i)

for i in range(5):
    n=int(input())
    S=str(n)
    l=len(S)
    sum=0
    for j in S:
        sum+=int(j)**l
    if sum==n:
        print(n,"is an armstrong number")
    else:
        print(n,"is not an armstrong number")
'''





        


