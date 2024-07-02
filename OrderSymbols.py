symbols=['$','!','*','^','<','>','~',' ']
input=['^','$','<','!']
#ctr=0
op=[]
for s in symbols:
    if s in input:
        #print(s,end=" ")
        op.append(s)
        #ctr+=1
    #if ctr==len(input):
    if len(op)==len(input):
        break
print(op)
