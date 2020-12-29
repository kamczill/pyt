from random import randint

imiona = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
imiona2 = [name[0] for name in imiona]
print(imiona2)

numbers = [[randint(1,10) for y in range(4)] for x in range(5)]
print(numbers)