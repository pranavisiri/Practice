n=int(input())
u=n%10
t=(n//10)%10
hu=n//100
res=(h**3)+(t**3)+(u**3)
if res==n:
    print("Yes")
else:
    print("No")
