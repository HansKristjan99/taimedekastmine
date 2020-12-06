import calendar, os, re, potilillede_kastmise_andmebaas
from calendar import monthrange
from random import randint
import datetime as dt
from termcolor import colored

path = os.getcwd()

    # kuupäevade määramine
time_now = dt.datetime.now()
time_after = time_now + dt.timedelta(days=monthrange(dt.datetime.now().year, dt.datetime.now().month)[1])
# kalendrite määramine
kal1 = calendar.TextCalendar(calendar.MONDAY)
kalender1 = kal1.formatmonth(time_now.year, time_now.month)
kal2 = calendar.TextCalendar(calendar.MONDAY)
kalender2 = kal2.formatmonth(time_after.year, time_after.month)
värvid = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'gray']

def kalender(intervall):
    global kalender1
    global kalender2
    global värvid
    paev, kuu, aasta = time_now.day, time_now.now().month, time_now.now().year
    kuu2, aasta2 = time_after.month, time_after.year
    for match in re.finditer(f'{time_now.year}', kalender1):
        end1 = match.end()
    for match in re.finditer(f'{time_after.year}', kalender2):
        end2 = match.end()
    punased1,punased2 = [],[]
    while paev <= calendar.monthrange(aasta, kuu)[1]:
        punased1.append(paev)
        paev += intervall
    paev -= calendar.monthrange(aasta, kuu)[1]
    while paev <= calendar.monthrange(aasta2, kuu2)[1]:
        punased2.append(paev)
        paev += intervall
    for el in punased1:
        kalender1 = re.sub(rf'\b{el}\b', str(el) + colored('*',värvid[0]), kalender1, 1)
    for el in punased2:
        kalender2 = re.sub(rf'\b{el}\b', str(el) + colored('*',värvid[0]), kalender2, 1)
    try:
        värvid.pop(0)
    except:
        värvid = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'gray']
    return (kalender1+kalender2)

database = f"{path}\\pythonsqlite.db"
conn = potilillede_kastmise_andmebaas.create_connection(database)
koruds = ''
while koruds != 'n':
    nimi = input("Sisesta taime nimi ladina keeles või sisesta 'kuva' kogu andmebaasi nägemiseks: ").capitalize()
    if nimi == 'Kuva':
        potilillede_kastmise_andmebaas.select_all_tables(conn)
    else:
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
            kordus = input("\nKas soovite veel lisada taimi (Y, N): ").lower()
            if kordus == 'n':
                break
