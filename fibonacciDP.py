#Tabulation approach
def fib(n):
    arr=[0]*(n+1)
    arr[1]=1
    for i in range(2,n+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr
n=int(input("enter n:"))
print("fibonacci series is",fib(n))

#Memoization approach
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    elif n==0 or n==1:
        return n
    else:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
        return memo[n]
def fib_series(n):
    fib_arr=[]
    for i in range(n+1):
        fib_arr.append(fib(i))
    return fib_arr
n=int(input())
fib(n)
print("fibonacci series is",fib_series(n))

#General approach
'''
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(1,n+1):
        c=a+b
        print(c)
        a=b
        b=c
n=int(input())
print(fib(n))
'''
