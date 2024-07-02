def factorial(n):
    arr=[0]*(n+1)
    arr[0]=1
    for i in range(1,n+1):
        arr[i]=arr[i-1]*i
    return arr[n]
n=int(input())
if n<0:
    print("factorial doest not exist")
else:
    print("factorial of given number is:",factorial(n))
