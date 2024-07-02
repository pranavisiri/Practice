ops=[]
n=int(input("no.of operations"))
while n>0:
    ops.append(input("Enter ops"))
    n=n-1
stack=[]
for i in ops:
    if i.isnumeric():
        stack.append(int(i))
    elif i=="C":
        stack.pop()
    elif i=="D":
        top=stack[-1]
        stack.append(2*top)
    elif i=="+":
        a=stack[-1]
        b=stack[-2]
        stack.append(a+b)
print(sum(stack))
