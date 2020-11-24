password = "krakow"
tries = 3
counter = 0
passwordIn = ''

while passwordIn != password:
    tries -= counter
    print('Masz jeszcze %d prob' % (tries))
    passwordIn = input('Podaj haslo: ')

    if passwordIn == password:
