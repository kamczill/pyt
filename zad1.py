#Proszę posortować podaną listę po drugim elemencie każdej listy, a w przypadku, kiedy są równe to po trzecim elemencie:

list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]

for x in range(3):
    for y in range(2):
        if list_to_sort[x][y+1]