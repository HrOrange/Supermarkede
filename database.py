#laver nogle databaser
#1. database til brugere
#2. database til vare
#3. database til så meget andet. føl .dia filen
import math
import random
import time
import sqlite3
from flask import g
import os

class Data:
    def __init__(self, navn):
        self.con = sqlite3.connect(navn + ."db")
        print("'Database åben'")
