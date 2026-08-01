def add_two_numbers() -> int:
    twonumber=input()
    listof2=twonumber.split(",")
    a=0
    for x in listof2:
        a +=int(x)
    return a



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
