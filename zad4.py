from random import randint
from time import perf_counter_ns

long_list = [randint(0, 3000) for element in range(1000000)]

start = perf_counter_ns()

#pomysl 1
for element in long_list:
    if element == -1:
        print("Element -1 należy do listy")
        break


stop = perf_counter_ns()
print ("Pierwsza operacja trwała ", stop-start, "nanoseconds\n")

i=0
number = 0

start = perf_counter_ns()
while number != -1:
    number = long_list[i]
    if number == -1:
        print("liczba -1 została znaleziona")
        break
    if i == len(long_list)-1:
        print("nie ma tej liczby w tej liście")
        break
    i += 1
stop = perf_counter_ns()
print ("Druga operacja trwała ", stop-start, "nanoseconds")
