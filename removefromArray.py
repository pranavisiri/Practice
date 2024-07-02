def remove(arr,e):
    k=0
    cnt=0
    for i in range(len(arr)):
        if arr[i]==e:
            cnt+=1
            continue
        else:
            arr[k]=arr[i]
            k=k+1
    for j in range(k,len(arr)):
        arr[j]='-'
    return arr
print(remove([2,3,4,5],3))
