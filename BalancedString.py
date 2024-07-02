s=input("enter exp:")
stack=[]
res=[]
br=1
for i in s:
    #print(i,end=" ")
    if i=='(':
        stack.append(br)
        res.append(br)
        br+=1
    elif i==')':
        temp=stack.pop()
        res.append(temp)
    else:
        pass
    
print(*res)
