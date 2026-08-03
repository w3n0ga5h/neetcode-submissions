from typing import Dict, List, Tuple


def get_dict_items(age_dict: Dict[str, int]) -> List[Tuple[str, int]]:
    name=age_dict.keys()
    name_list=list(name)
    age=age_dict.values()
    agelist=list(age)
    return name_list,agelist

# do not modify below this line
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40}))
print(get_dict_items({'Bob': 30, 'David': 40, 'Charlie': 35, 'Alice': 25, 'Eve': 45}))
print(get_dict_items({'Alice': 25, 'Bob': 30, 'Charlie': 35, 'David': 40, 'Eve': 45, 'Frank': 50}))
