from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    final_list=[]
    for listing in nested_arr:
        a=0
        for numbs in listing:
            if numbs > a:
                a=numbs 
            


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
