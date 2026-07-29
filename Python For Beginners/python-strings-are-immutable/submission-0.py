def remove_fourth_character(word: str) -> str:
    before4 = word[:4]
    after4 = word[5:]
    return before4+after4


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
