import math
from enum import Enum

#her laver vi et par ekstra funktioner som gør det nemmere i main.

class roller(Enum):
    #ligegyldige
    service_medarbejder = 0
    kasse_dame = 1

    #medium
    kiosk = 2
    vin_mand = 3
    slagter = 4
    delikatesse_medarbejder = 5

    #VIP's, aka, the cool kids
    lukke_ansvarlig = 6
    butiks_chef = 7
    købmand = 8


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
