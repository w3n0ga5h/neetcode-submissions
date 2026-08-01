from typing import List

def read_integers() -> List[int]:
    mylist=input()
    stringlist=mylist.split(",")
    listlist=list(stringlist)
    return listlist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
