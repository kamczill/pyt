#Proszę posortować podaną listę po drugim elemencie każdej listy, a w przypadku, kiedy są równe to po trzecim elemencie:

def sort(list_to_sort):
    for x in range(len(list_to_sort)):
        for y in range(x+1,len(list_to_sort)):
            if list_to_sort[x][1] != list_to_sort[y][1]:
                if list_to_sort[x][1] > list_to_sort[y][1]:
                    tmp = list_to_sort[y]
                    list_to_sort[y] = list_to_sort[x]
                    list_to_sort[x] = tmp
            else:
                if list_to_sort[x][2] > list_to_sort[y][2]:
                    tmp = list_to_sort[y]
                    list_to_sort[y] = list_to_sort[x]
                    list_to_sort[x] = tmp


list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]

sort(list_to_sort)
print(list_to_sort)

list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]

sort(list_to_sort_2)
print(list_to_sort_2)