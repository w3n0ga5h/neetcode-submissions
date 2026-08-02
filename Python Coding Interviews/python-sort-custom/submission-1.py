from typing import List

def intlength(numb: int):
    return abs(numb)
def strlength(stra: str):
    return len(stra)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=strlength,reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=intlength)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
