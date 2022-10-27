from datetime import date

today = date.today()
# today = date(2022, 10, 28) # Vineri
day = today.isoweekday() # Returneaza ziua saptamanii ca int (1 - 7)
oreValabile = []

if day != 5:
    if day == 6:
        dataValabila = str(int(today.strftime('%d')) + 2) + '.' + \
                       today.strftime('%m.%y')
    else:
        dataValabila = str(int(today.strftime('%d')) + 1) + '.' + \
                       today.strftime('%m.%y')
    print('Pentru programare sunt libere urmatoarele ore din data de '
          + str(dataValabila) + ':')
    for i in range(8, 20):
        oreValabile.append(str(i) + ':00')
        oreValabile.append(str(i) + ':30')
else:
    dataValabila = str(int(today.strftime('%d')) + 1) + '.' + today.strftime('%m.%y')
    print('Pentru programare sunt libere urmatoarele ore din data de '
          + str(dataValabila) + ':')
    for i in range(8, 15):
        oreValabile.append(str(i) + ':00')
        oreValabile.append(str(i) + ':30')

print(*oreValabile, sep = ", ")

inputUser = input('Introduceti ora: ')

oraProgramata = False

while oraProgramata == False:
    if inputUser == 0:
        oraProgramata = True
    elif inputUser in oreValabile:
        print('Programare memorata')
        oraProgramata = True
    else:
        print('Introduceti alta ora.')
        print(*oreValabile, sep = ", ")
        inputUser = input('Introduceti ora: ')
