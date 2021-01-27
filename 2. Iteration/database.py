import math
import random
import time
import sqlite3
import os

class Data:
    def __init__(self, navn, columns = None, randoms = None):
        database_exist = os.path.exists(os.getcwd() + '\\' + navn + ".db")
        print(str(navn) + " : " + str(database_exist))

        self.colum_titles = [x.split(' ')[0] for x in columns]
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
            command = 'INSERT INTO ' + navn + ' ('
            for x in range(len(self.colum_titles) - 1):
                command += self.colum_titles[x] + ', '
            command += self.colum_titles[-1] + ') VALUES (' + '?,' * (len(self.colum_titles) - 1) + '?)'

            c = self.con.cursor()
            for r in randoms:
                c.execute(command, r)
            self.con.commit()
        else:
            print(navn + '.db eksisterer')

    def insert(self, data):
        #TODO: tilføj data til database
        c = self.con.cursor()
        #call insert
    def remove(self, data):
        #TODO: fjern data fra database
        c = self.con.cursor()
        #call remove

    def find(self, kolonner, data, get = None):
        if get != None:
            if get not in self.colum_titles:
                return False

        t = ""
        for i in range(len(kolonner) - 1):
            t += kolonner[i] + ","
        t += kolonner[-1]

        if get != None:
            t += "," + get

        #print('SELECT ' + t + ' FROM ' + self.navn)
        c = self.con.cursor()
        c.execute('SELECT ' + t + ' FROM ' + self.navn)

        a = False
        for x in c:
            a = True
            for i in range(len(data)):
                #print(x[i])
                #print(data[i])
                if data[i] != str(x[i]):
                    a = False
                    break

            if a == True:
                if get != None:
                    return x[-1]
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

        s.column_names = {}
        s.column_types = {}
        s.randoms = {}
        for i in range(len(names)):
            s.column_names[names[i]] = column_names[i]
            s.column_types[names[i]] = column_types[i]
            s.randoms[names[i]] = randoms[i]

        s.tabel_names = names
        print(s.tabel_names)
        #['Joachim','1234'], ['Nicolai', '4321'], ['Michael', '1'], ['Alexander', '2'], ['Anders', '3']
        for i in range(len(names)):
            try:
                command = "CREATE TABLE " + str(names[i]) + " (ID INTEGER PRIMARY KEY, "
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
                for r in randoms[i]:
                    s.c.execute(command, r)
                s.con.commit()
            except:
                print('Tabellen ' + names[i] + ' allerede')

    def find(s, tabel, kolonner, data, get = None):
        if get != None:
            if get not in s.column_names[tabel]:
                return False

        t = ''
        for i in range(len(kolonner) - 1):
            t += kolonner[i] + ','
        t += kolonner[-1]

        if get != None:
            t += "," + get

        c = s.con.cursor()
        c.execute('SELECT ' + t + ' FROM ' + tabel)

        for x in c:
            a = True
            for i in range(len(data)):
                if data[i] != str(x[i]):
                    a = False
                    break
            if a:
                if get != None:
                    return x[-1]
                break

        return a
    def find_quick(s, tabel, kolonner, data, get = None):
        pass
    def find_with_links(s, linking_tabel, link_kolonner_1, link_kolonner_2, data, get = None, get_origin = None):
        #skal laves meget lig funktionen find, men tabeller skal linkes (det er hvad Søren ville kalde En-til-mange vi taler om her: http://bog.laerpython.dk/da/latest/ch-database/sqlite-advanced.html#en-til-mange-relation)

        #et eksempel kunne være i forhold til hvilke vagter der tilhørte hvilke ansatte.
        #linking_tabel kunne være 'VagtLink'
        #link_kolonner_1 kunne være ['VagtLink.PersonID', 'VagtLink.VagtID']
        #link_kolonner_1 kunne være ['Ansatte.ID', 'Vagt.ID']
        #data ville være noget som ['Peter', 124.4, 13]
        #get kunne være 'Kodeord' og get_origin kunne være 'Ansatte'
        pass
    def add_tabel(s, tabel_name, tabel_colums):
        #TODO: brug kommandoen "CREATE TABLE [table_name] (something, something, something) guide kan findes på lærpython.dk
        c = s.con.cursor()
        print(tabel_name)
        print(tabel_colums)
        command = 'CREATE TABLE ' + str(tabel_name) + ' (id INTERGER PRIMARY KEY,'
        for x in range(len(tabel_colums) - 1):
            command += tabel_colums[x] + ','
        command += tabel_colums[-1] + ')'
        print(command)
        c.execute(command)
        s.tabel_names.append(tabel_name)

    def insert(s, tabel_name, colum_names, data):
        #TODO: tilføj data til database
        command = 'INSERT INTO ' + tabel_name + '('
        for x in range(len(colum_names) - 1):
            command += colum_names[x] + ','
        command += colum_names[-1] + ') VALUES ('
        command += '?,' * (len(data) - 1) + '?)'
        print(command)
        s.con.execute(command,data)
        s.con.commit()

    def remove(s, data):
        #TODO: fjern data/person/something fra database
        pass
    def get_length(s, tabel):
        c = s.con.cursor()
        c.execute('SELECT * FROM ' + tabel)
        count = 0
        for x in c:
            count += 1
        return count
    def print(s, tabel = None):
        if len(s.tabel_names) == 0:
            print()
            return
        c = s.con.cursor()

        largest_tabel = 0
        if tabel == None:
            for i in s.tabel_names:
                c.execute('SELECT * FROM ' + i)
                for j in c:
                    if len(j) > largest_tabel:
                        largest_tabel = len(j)
                    break
        else:
            c.execute('SELECT * FROM ' + tabel)
            for j in c:
                if len(j) > largest_tabel:
                    largest_tabel = len(j)
                break

        p = '\n' + "#" * 40 + "\n"
        for i in range(len(s.tabel_names) - 1):
            t = math.floor(((largest_tabel * 3) - len(s.tabel_names[i])) / 2 + 1)
            p += ('-' * t * 2) + s.tabel_names[i] + ('-' * t * 2) + "\n"
            c.execute('SELECT * FROM ' + s.tabel_names[i])
            for j in c:
                print(j)
                for k in range(len(j) - 1):
                    p += str(j[k]) + " | "
                p += str(j[-1]) + "\n"
            p += "\n"

        t = math.floor(((largest_tabel * 3) - len(s.tabel_names[-1])) / 2 + 1)
        p += ('-' * t * 2) + s.tabel_names[-1] + ('-' * t * 2) + "\n"
        c.execute('SELECT * FROM ' + s.tabel_names[-1])
        for j in c:
            print(j)
            for k in range(len(j) - 1):
                p += str(j[k]) + " | "
            p += str(j[-1]) + "\n"

        p += "#" * 40 + '\n'

        print(p)
    def __str__(s):
        if len(s.tabel_names) == 0:
            return ''
        c = s.con.cursor()

        largest_tabel = 0
        for i in s.tabel_names:
            c.execute('SELECT * FROM ' + i)
            for j in c:
                if len(j) > largest_tabel:
                    largest_tabel = len(j)
                break

        p = '\n' + "#" * 40 + "\n"
        for i in range(len(s.tabel_names) - 1):
            t = math.floor(((largest_tabel * 3) - len(s.tabel_names[i])) / 2 + 1)
            p += ('-' * t * 2) + s.tabel_names[i] + ('-' * t * 2) + "\n"
            c.execute('SELECT * FROM ' + s.tabel_names[i])
            for j in c:
                print(j)
                for k in range(len(j) - 1):
                    p += str(j[k]) + " | "
                p += str(j[-1]) + "\n"
            p += "\n"

        t = math.floor(((largest_tabel * 3) - len(s.tabel_names[-1])) / 2 + 1)
        p += ('-' * t * 2) + s.tabel_names[-1] + ('-' * t * 2) + "\n"
        c.execute('SELECT * FROM ' + s.tabel_names[-1])
        for j in c:
            print(j)
            for k in range(len(j) - 1):
                p += str(j[k]) + " | "
            p += str(j[-1]) + "\n"

        p += "#" * 40 + '\n'

        return p
'''users_data = Data("users", columns = ['navn STRING', 'password STRING', 'rolle INT'], randoms = [['Joachim','1234', 14], ['Nicolai', '4321', 2], ['Michael', '1', 5], ['Alexander', '2', 6], ['Anders', '3', 9]])
users_data.print()
print(users_data.find(["navn", "password"], ["Nicolai","4321"], get = 'peter'))'''

'''data1 = Data_Alternative()
data1.add_tabel("Katte", ['kat1 STRING', 'katte5 INT'])
for x in range(5):
    data1.insert('Katte', ['kat1','katte5'], ['Joachim er bedre end Nicolai', 5])
print(str(data1))'''


'''data = Data_Alternative(
names = ["test_1", "test_2"],
column_names = [['col_1', 'col_2', 'col_3', 'col_4'],  ['trar', 'jiajwd']],
column_types = [['STRING', 'INT', 'INT', 'STRING'],  ['STRING', 'INT']],
randoms = [[['peter', 5, 10, 'hej'], ['lars', 2000, 10, 'peter']], [['peter', 5], ['lars', 2000]]])
print(str(data))'''
