from typing import List, Tuple

a= 0
def best_student(scores: List[Tuple[str, int]]) -> str:
    a=0
    listfinal=[]
    for x, y in scores:
        print(f"x: {x}, y: {y}")
        listfinal.append(y)
        print(listfinal)
    
# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
