import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap=[]
    finallist=[]
    for x in nums:
        pair=(-x,x)
        heapq.heappush(heap,pair)
    print (heap)
    while heap:
        pair=heapq.heappop(heap)
        finallist.append(pair[1])
    return finallist


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
