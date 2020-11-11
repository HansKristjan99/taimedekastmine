import calendar, os, potilillede_kastmise_andmebaas
import datetime as dt
from termcolor import colored

path = os.getcwd()

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

database = f"{path}\pythonsqlite.db"
conn = potilillede_kastmise_andmebaas.create_connection(database)

nimi = input("Sisesta taime nimi ladina keeles või sisesta 'kuva' kogu andmebaasi nägemiseks: ")
if nimi == "kuva":
    potilillede_kastmise_andmebaas.select_all_tables(conn)
try:
    kastmis_intervall = potilillede_kastmise_andmebaas.select_intervall(conn, nimi)[0]
except TypeError:
    print("Sellist taime meie andmebaasis ei leidu.")
    vastus = input("Kas soovid seda taime andmebaasi lisada? (Sisesta Y või N) ").lower()
    if vastus == "y":
        intervall = input("Sisesta kastmise intervall: ")
        with conn:
            taim = (nimi, intervall)
            potilillede_kastmise_andmebaas.create_taim(conn, taim)
        print("Taim sisestatud andmebaasi.")
else:
    print(kalender(kastmis_intervall))