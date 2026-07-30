from typing import List

def contains_duplicate(words: List[str]) -> bool:
    myset=set()
    print(myset)
    for elements in words:
        myset.add(elements)
        if myset:
            continue
        else:
            return 0
    return len(myset)
# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
