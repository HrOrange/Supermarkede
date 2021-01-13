import math
import random
import time
import sqlite3
import os

class Data:
    def __init__(self, navn, table_columns = None, randoms = None):
        database_exist = os.path.exists(os.getcwd() + '\\' + navn + ".db")

        self.navn = navn
        self.con = sqlite3.connect(navn + ".db")

        if database_exist == False:
            print(navn + '.db eksisterer ikke')

            #lav tablen. Der er alt for meget string manipulation i SQL
            command = "CREATE TABLE " + str(navn) + " (ID INTEGER PRIMARY KEY AUTOINCREMENT, "
            for x in range(len(table_columns) - 1):
                command += table_columns[x] + ", "
            command += table_columns[-1] + ")"
            self.con.execute(command)

            #Indsæt noget dummy data. BTW dummy dataen skal gives fra main igennem init paramaterne
            colum_titles = [x.split(' ')[0] for x in table_columns]
            command = 'INSERT INTO ' + navn + ' ('
            for x in range(len(colum_titles) - 1):
                command += colum_titles[x] + ', '
            command += colum_titles[-1] + ') VALUES (' + '?,' * (len(colum_titles) - 1) + '?)'

            c = self.con.cursor()
            for r in randoms:
                c.execute(command, r)
            self.con.commit()
        else:
            print(navn + '.db eksisterer')

    def insert(self, data):
        #TODO: tilføj data til database
        pass
    def remove(self, data):
        #TODO: fjern data/person/something fra database
        pass
    def find(self, data):
        #TODO: check om data er i database og returner True eller False
        pass
    def get_length(self): #jeg hader denne solution
        c = self.con.cursor()
        c.execute('SELECT * FROM ' + self.navn)
        count = 0
        for x in c:
            count += 1
        return count

    def print(self): #bare en print funktion der printer det data der er i databasen
        c = self.con.cursor()
        c.execute('SELECT * FROM ' + self.navn)
        for x in c:
            print(x)

    #Joachim lavede dette (Hvordan tager jeg længden af den ønskede database, hvilket er users.db)
    def check_user(self, navn, password):
        c = self.con.cursor()
        c.execute('SELECT * FROM ' + self.navn) #gætter på du gerne vil have noget data fra din database du kan tjække igennem

        for i in range(0, self.get_length()):
            pass
            #print(1)
        return True

class Data_Alternative:
    def __init__(s):
        s.m_con = sqlite3.connect(navn + ".db")
    def add_database(s, database_name):
        pass
    def __str__(s):
        pass
