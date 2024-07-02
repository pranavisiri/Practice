n=int(input())
arr=[1,2,3,4,5]
brr=[5,4,3,2,1]
a=0
b=0
x=3
y=3
sum=0
for i in range(n):
    d=arr[i]-brr[i]
    if (d>=0 and a<x)or b>=y:
        sum+=arr[i]
        a+=1
        print(sum)
    else:
        sum+=brr[i]
        b+=1
        print(sum)
    else:
        if a>=b:
            
    if (arr[i]>=brr[i] and a<x) or b==y:
        sum=arr[i]
        a+=1
    else:
        sum+=brr[i]
        b+=1
        

print(sum)
