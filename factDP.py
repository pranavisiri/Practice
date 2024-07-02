def fact(n,memo={}):
    if n in memo:
        return memo[n]
    elif n==0:
        return 1
    else:
        memo[n]=n*fact(n-1,memo)
        return memo[n]
n=int(input())
if n<0:
    print("factorial doesn't exit")
else:
    print("factorial of given number is: ",fact(n))
