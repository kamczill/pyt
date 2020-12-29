password = "krakow"
tries = 5
counter = 0
passwordIn = ''

while counter != tries:
    print('\n\nIlosc prób: %d' % (tries-counter))
    passwordIn = input('Podaj haslo: ')
    counter += 1
    if passwordIn == password:
        break
    else:
        print('\nHaslo nieprawidlowe')


if counter == tries:
    print('\nNie udało Ci sie zgadnąć hasła ;c')
else:
    print('\nGRATULACJE!!! Hasło to %s. Udało Ci się zgadnąć w %d próbach' % (password, counter))