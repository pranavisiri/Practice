#Memoization approach
def sumN(n,memo={}):
    if n in memo:
        return memo[n]
    elif n==0:
        return 0
    else:
        memo[n]=n+sumN(n-1,memo)
        return memo[n]
n=int(input())
print("sum of N numbers is:",sumN(n))


#Tabulation approach
def sumN(n):
    arr=[0]*(n+1)
    for i in range(1,n+1):
        arr[i]=arr[i-1]+i
    return arr[n]
n=int(input())
print("sum of N is:",sumN(n))



#general approach
'''def sumN(n):
    sum=0
    if n==0:
        return 0
    else:
        for i in range(1,n+1):
            sum=sum+i
        return sum
n=int(input())
print("sum of N numbers is:",sumN(n))'''
        
