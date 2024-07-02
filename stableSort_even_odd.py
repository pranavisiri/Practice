'''stable sort of even odd values in an array.
stable means arranging the values based on their order'''

def stablesort(arr):
    i=0
    j=0
    while i<len(arr):
        if arr[i]%2==0:
            x=arr.pop(i)
            arr.insert(j,x)
            j=j+1
        i=i+1
    print(arr)
stablesort([7,6,2,4,9,11,3,8])


'''
def stable_even_odd(arr):
    n = len(arr)
    next_even_pos = 0

    for i in range(n):
        if arr[i] % 2 == 0:
            even_num = arr[i]
            # Shift all elements from next_even_pos to i-1 to the right by one position
            for j in range(i, next_even_pos, -1):
                arr[j] = arr[j - 1]
            # Place the even number at the next_even_pos
            arr[next_even_pos] = even_num
            next_even_pos += 1

    return arr
# Test cases
print(stable_even_odd([7,6,2,4,9,11,3,8]))     # Output: [6,2 4,8,7,9,11,3]
print(stable_even_odd([int(x) for x in input().split()]))     # Output: [4, 2, 8, 3, 7, 5]
print(stable_even_odd([10, 21, 32, 43, 54]))   # Output: [10, 32, 54, 21, 43]
'''
    
    
    
