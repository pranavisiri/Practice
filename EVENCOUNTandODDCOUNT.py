str="11,45,22,27,32,45,72,78,83"
l=str.split(",")
#l=[int(x) for x in str.split(",")]
#l=list(map(int,str.split(",")))
print(l)
evenC=0
oddC=0
for i in l:
    if int(i)%2==0:
        evenC+=1
    else:
        oddC+=1
        
#print(evenC,oddC)
tuple=(evenC,oddC)
print(tuple)
