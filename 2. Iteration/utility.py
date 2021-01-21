import math
from enum import Enum

#her laver vi et par ekstra funktioner som gør det nemmere i main.

class roller(Enum):
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
    købmand = 10


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
