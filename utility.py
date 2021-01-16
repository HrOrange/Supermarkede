import math
from enum import Enum

#her laver vi et par ekstra funktioner som gør det nemmere i main.

class roller(Enum):
    kunde = 0
    ansat = 1
    boss = 2

''' Disse eksempler skulle gøre rolle enummen foroven nemmere at forstår
peter = ('peter', 16, roller.ansat)
print(peter)
print(roller.ansat.value)
print(roller.ansat.name)'''


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
