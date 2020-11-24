from random import randint

long_list = [randint(0, 3000) for element in range(1000000)]

for element in long_list:
    if element == -1:
        print("Element -1 należy do listy")
        break
