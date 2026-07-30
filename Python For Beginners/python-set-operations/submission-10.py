from typing import List

def count_unique_words(words: List[str]) -> int:
    myset=set()
    for elements in words:
        myset.add(elements)
        if myset:
            continue
        else:
            return 0
    return len(myset)
# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
