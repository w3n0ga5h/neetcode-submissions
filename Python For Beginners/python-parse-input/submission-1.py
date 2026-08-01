from typing import List

def read_integers() -> List[int]:
    mylist=input()
    listlist=[]
    stringlist=mylist.split(",")
    for x in stringlist:
        listlist.append(int(x))
    return listlist

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
