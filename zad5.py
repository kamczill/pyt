from random import randint

imiona = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
imiona2 = []

for name in imiona:
    imiona2.append(name[0])

print(imiona2)

randomNum = []
num = 0
for i in range(5):
        randomNum2 = [randint(1,10) for el in range(4)]
        randomNum.append(randomNum2)

print(randomNum)