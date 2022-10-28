from datetime import date
from datetime import datetime

zileDeNastere = []
for i in range(0, 2):
    arrayDate = []
    x = input('Zi de nastere: ')
    for j in x.split("."):
        arrayDate.append(j)
    zileDeNastere.append(date(2023, int(arrayDate[1]), int(arrayDate[0])))

zi1 = int(zileDeNastere[0].strftime('%j'))
zi2 = int(zileDeNastere[1].strftime('%j'))
ziMijloc = (zi1 + zi2) // 2

dataFinala = datetime.strptime('2023' + "-" + str(ziMijloc), "%Y-%j").strftime("%d-%m-%Y")
print('Te invitam la petrecerea noastra pe ' + dataFinala + ' la ora 19, in Bistro H')