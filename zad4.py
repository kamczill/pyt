from random import randint
import time

long_list = [randint(0, 3000) for element in range(1000000)]

start_time = time.clock()
for element in long_list:
    if element == -1:
        print("Element -1 należy do listy")
        break
print (time.clock() - start_time, "seconds")

i=0
number = 0

while number != -1:
    number = long_list[i]
    if number == -1:
        print("liczba -1 została znaleziona")
        break
    if i == len(long_list)-1:
        print("nie ma tej liczby w tej liście")
        break
    i += 1

