# it count the particular itoem in litst

def list_count(nums):
    count = 0 
    for num in nums:
        if num == 44:
            count+= 1
    return count

print(list_count([1,2,3,4,5,6,4,4,4,33,4,4,4,4,6,7,44]))    