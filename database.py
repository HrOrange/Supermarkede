import math
import random
import time
import sqlite3
import os

class Data:
    def __init__(self, navn, columns = None, randoms = None):
        database_exist = os.path.exists(os.getcwd() + '\\' + navn + ".db")

        self.navn = navn
        self.con = sqlite3.connect(navn + ".db")

        if database_exist == False:
            print(navn + '.db eksisterer ikke')

            #lav tablen. Der er alt for meget string manipulation i SQL
            command = "CREATE TABLE " + str(navn) + " (ID INTEGER PRIMARY KEY AUTOINCREMENT, "
            for x in range(len(columns) - 1):
                command += columns[x] + ", "
            command += columns[-1] + ")"
            self.con.execute(command)

            #Indsæt noget dummy data. BTW dummy dataen skal gives fra main igennem init paramaterne
            colum_titles = [x.split(' ')[0] for x in columns]
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

    def find(self, kolonne, data):
        t = ""
        for i in range(len(kolonne) - 1):
            t += kolonne[i] + ","
        t += kolonne[-1]

        #print('SELECT ' + t + ' FROM ' + self.navn)
        c = self.con.cursor()
        c.execute('SELECT ' + t + ' FROM ' + self.navn)

        for x in c:
            a = True
            for i in range(len(data)):
                #print(x[i])
                #print(data[i])
                if data[i] != str(x[i]):
                    a = False
                    break

            if a == True:
                break

        return a



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


class Data_Alternative:
    def __init__(s, names = [], column_names = [], column_types = [], randoms = []):
        s.con = sqlite3.connect("data.db")
        s.c = None

        #['Joachim','1234'], ['Nicolai', '4321'], ['Michael', '1'], ['Alexander', '2'], ['Anders', '3']
        for i in range(len(names)):
            try:
                command = "CREATE TABLE " + str(names[i]) + " (ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                for x in range(len(column_names[i]) - 1):
                    command += column_names[i][x] + ' ' + column_types[i][x] + ", "
                command += column_names[i][-1] + ' ' + column_types[i][x] + ")"
                s.con.execute(command)

                #Indsæt noget dummy data. BTW dummy dataen skal gives fra main igennem init paramaterne
                command = 'INSERT INTO ' + names[i] + ' ('
                for x in range(len(column_names[i]) - 1):
                    command += column_names[i][x] + ', '
                command += column_names[i][-1] + ') VALUES (' + '?,' * (len(column_names[i]) - 1) + '?)'

                s.c = s.con.cursor()
                for r in randoms:
                    s.c.execute(command, r)
                s.con.commit()
            except:
                print('Tabellen ' + names[i] + ' allerede')

    def find(s, tabel, kolonner, data):
        t = ''
        for i in range(len(kolonne) - 1):
            t += kolonne[i] + ','
        t += kolonne[-1]

        c = s.con.cursor()
        c.execute('SELECT ' + t + ' FROM ' + tabel)

        for x in c:
            a = True
            for i in range(len(data)):
                if data[i] != str(x[i]):
                    a = False
                    break
            if a:
                break

        return a
    def add_tabel(s, tabel_name):
        pass
    def __str__(s):
        pass

#users_data = Data("users", columns = ['navn STRING', 'password STRING'], randoms = [['Joachim','1234'], ['Nicolai', '4321'], ['Michael', '1'], ['Alexander', '2'], ['Anders', '3']])
#users_data.print()
#print(users_data.find(["navn", "password"], ["Nicolai","4321"]))
