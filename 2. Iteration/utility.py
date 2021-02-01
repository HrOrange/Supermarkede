import math
import enum
import sqlite3
import database
import time

#her laver vi et par ekstra funktioner som gør det nemmere i main.
def swap(a, b):
    return b, a
def reverse(a):
    return [a[len(a) - x - 1] for x in range(len(a))]
def rank(l, ranks, return_both = True):
    b = []
    c = []
    length = len(l)
    for i in range(length):
        lowest = min(ranks)
        for j in range(length):
            if ranks[j] == lowest:
                b.append(l[j])
                c.append(ranks[j])
                ranks.remove(ranks[j])
                l.remove(l[j])
                break
    if return_both:
        return b, c
    else:
        return b
def sort_list(l):
    new_l = []
    a = len(l)
    for i in range(a):
        lowest_index = 0
        for j in range(1, len(l)):
            if l[j] < l[lowest_index]:
                lowest_index = j
        new_l.append(l[lowest_index])
        l.remove(l[lowest_index])
    return new_l

'''class roller(enum.Enum):
    #ingen rolle
    ingen = 0
    kunde = 1

    #ligegyldige
    service_medarbejder = 2
    kasse_dame = 3

    #medium
    kiosk = 4
    vin_mand = 5
    slagter = 6
    delikatesse_medarbejder = 7

    #VIP's, aka, the cool kids
    lukke_ansvarlig = 8
    butiks_chef = 9
    købmand = 10'''

rolle_data = database.Data_Alternative(
names = ['roller'],
column_names = [['rolle', 'rank']],
column_types = [['STRING', 'INT']],
not_nulls = [[True, None]],
randoms = [[['ingen', 1], ['kunde', 2], ['service_medarbejder', 3], ['kasse_dame', 4], ['kiosk', 5], ['vin_mand', 6], ['slagter', 7], ['delikatesse_medarbejder', 8], ['lukke_ansvarlig', 9], ['butiks_chef', 10], ['købmand', 11]]])
print(str(rolle_data))

c = rolle_data.con.cursor()
c.execute('SELECT * FROM roller')
names = []
ranks = []
for x in c:
    names.append(x[1])
    ranks.append(x[2])
#names = [m.name for m in util.roller] + ['newname1', 'newname2']
roller = enum.Enum('roller', rank(names, ranks, return_both = False))


def get_rolle_name(index):
    for r in roller:
        if r.value == index:
            return r.name
def get_rolle_index(name):
    for r in roller:
        if r.name == name:
            return r.value
def save_roller():
    c = rolle_data.con.cursor()
    c.execute('DELETE FROM roller')

    ranks = []
    names = []
    for r in roller:
        names.append(r.name)
        ranks.append(r.value)
    ranked_names, ranked_ranks = rank(names, ranks)
    combined = [[x, y] for x, y in zip(ranked_names, ranked_ranks)]

    for i in range(len(combined)):
        c.execute('INSERT INTO roller (rolle, rank) VALUES (?, ?)', combined[i])
    rolle_data.con.commit()

''' #Disse eksempler skulle gøre rolle enummen foroven nemmere at forstår
peter = ('peter', 16, roller.service_medarbejder)
print(peter)
print(roller.service_medarbejder.value)
print(roller.service_medarbejder.name)'''

class tidspunkt:
    def __init__(s, year, month, day, hour, minute, second):
        s.year = year
        s.month = month
        s.day = day
        s.hour = hour
        s.minute = mintute
        s.second = second
        s.time_stamp = str(year) + ":" + str(month) + ":" + str(hour) + ":" + str(minute) + ":" + str(second)
    def print(s):
        print(s.time_stamp)
