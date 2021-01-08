import math

#her laver vi et par ekstra funktioner som gør det nemmere i main.


class tidspunkt:
    def __init__(s, year, month, second):
        s.yea = year
        s.mon = month
        s.sec = second
        s.timestamp = str(year) + ":" + str(month) + ":" + str(second)
