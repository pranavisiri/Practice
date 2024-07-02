"""u are given an array where if there are elements between 6 and 7 that elements should
be skipped and rest elements should be added and if 6 is not there in the array add all the
elements and if 7 comes first in the array before 6 then also add all the values and if 6
is there and 7 is not there add the elements of the array before 6 give python code"""

def total(nums):
    s=0
    if 6 in nums and 7 in nums:
        i1=nums.index(6)
        i2=nums.index(7)
        if i1<i2:
            s=sum(nums[:i1])+sum(nums[i2+1:])
        else:
            s=sum(nums)
    elif 6 in nums and 7 not in nums:
        i=nums.index(6)
        s=sum(nums[:i])
    else:
        s=sum(nums)
    return s
nums=[1,3,5,6,8,9]
print(total(nums))
