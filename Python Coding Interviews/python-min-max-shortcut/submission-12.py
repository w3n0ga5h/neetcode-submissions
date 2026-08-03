from typing import List


def disallow_negatives(num: int) -> int:
    pass


def max_difference(nums: List[int]) -> int:
    limit=len(nums)-1
    a=0
    for x in range (len(nums)):
        n= x+1
        n= min(limit,n)
        result= nums[n]-nums[x]
        if result > a :
            a = result
    return a



# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
