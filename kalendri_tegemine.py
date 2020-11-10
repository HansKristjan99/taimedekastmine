import calendar
import datetime as dt
from termcolor import colored
def kalender(intervall):
    paev, kuu, aasta = dt.datetime.now().day, dt.datetime.now().month, dt.datetime.now().year
    kalender1=(calendar.month(aasta, kuu))
    if kuu==12:
        kuu2= 1
        aasta2 = aasta+1
        kalender2 = calendar.month(aasta2,1)
    elif kuu !=12:
        aasta2 = aasta
        kuu2 = kuu+1
        kalender2 = calendar.month(aasta,kuu2)
    punased1,punased2 = [],[]
    while paev <= calendar.monthrange(aasta, kuu)[1]:
        punased1.append(paev)
        paev += intervall
    paev -= calendar.monthrange(aasta, kuu)[1]
    while paev <= calendar.monthrange(aasta2, kuu2)[1]:
        punased2.append(paev)
        paev+= intervall
    for i in punased1:
        kalender1 = kalender1[:20] +kalender1[20:].replace(str(i),colored(i,"red"),1)
    for j in punased2:
        kalender2 = kalender2[:20] + kalender2[20:].replace(str(j), colored(j, "red"), 1)
    return (kalender1+kalender2)

print(kalender(4))
