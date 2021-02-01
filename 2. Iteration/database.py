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

    def insert(self, data, kolonner):
        #TODO: tilføj data til database
        c = self.con.cursor()
        #call insert
        p = "INSERT INTO " + self.navn + "("

        for x in range(len(kolonner) - 1):
            p += str(kolonner[x]) + ","
        p += str(kolonner[-1]) + ") VALUES (" + "?," * (len(data)-1) + "?)"
        print(p)

        c.execute(p,data)
        self.con.commit()


    def remove(self, kolonner, data, get = None):
        #TODO: fjern data fra database




        c = self.con.cursor()
        c.execute('DELETE FROM ' + self.navn + 'WHERE id = ')
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
    def __init__(s, names = [], column_names = [], column_types = [], defaults = [], not_nulls = [], randoms = []):
        #remembering the parameters
        s.tabel_names = names
        s.column_names = {}
        s.column_types = {}
        s.randoms = {}
        s.defaults = []
        s.not_nulls = []
        for i in range(len(names)):
            if len(defaults) == len(names):
                if len(defaults[i]) > 0:
                    s.defaults.append(defaults[i])
                else:
                    s.defaults.append([None for y in range(len(column_names[i]))])
            else:
                s.defaults.append([None for y in range(len(column_names[i]))])
            if len(not_nulls) == len(names):
                if len(not_nulls[i]) > 0:
                    s.not_nulls.append(not_nulls[i])
                else:
                    s.not_nulls.append([None for y in range(len(column_names[i]))])
            else:
                s.not_nulls.append([None for y in range(len(column_names[i]))])

        if len(names) > 0:
            name = ''
            for n in range(len(names) - 1):
                name += names[n] + '_'
            name += names[-1]
            s.con = sqlite3.connect(name + ".db")
            s.c = None

            for i in range(len(names)):
                try:
                    command = "CREATE TABLE " + str(names[i]) + " (ID INTEGER PRIMARY KEY, "
                    for x in range(len(column_names[i]) - 1):
                        if s.defaults[i][x] != None or s.not_nulls[i][x] != None:
                            command += column_names[i][x] + ' ' + column_types[i][x]

                            if s.defaults[i][x] != None:
                                command += ' DEFAULT ' + str(s.defaults[i][x])
                            if s.not_nulls[i][x] != None:
                                command += ' NOT NULL'

                            command += ','
                        else:
                            command += column_names[i][x] + ' ' + column_types[i][x] + ", "

                    if s.defaults[i][-1] != None or s.not_nulls[i][-1] != None:
                        command += column_names[i][-1] + ' ' + column_types[i][-1]
                        if s.defaults[i][-1] != None:
                            command += ' DEFAULT ' + str(s.defaults[i][-1])
                        if s.not_nulls[i][-1] != None:
                            command += ' NOT NULL'
                        command += ')'
                    else:
                        command += column_names[i][-1] + ' ' + column_types[i][-1] + ')'
                    #print(command)
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
                    print('Succesfully created ' + names[i])
                except:
                    print('Tabel ' + names[i] + ' eksisterede allerede.')

                s.column_names[names[i]] = column_names[i]
                s.column_names[names[i]].insert(0, 'ID')
                s.column_types[names[i]] = column_types[i]
                s.column_types[names[i]].insert(0, 'INT')
                s.randoms[names[i]] = randoms[i]
        else:
            s.con = sqlite3.connect("Default.db")
            s.c = None
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
                if data[i] != x[i]:
                    a = False
                    break
            if a:
                if get != None:
                    return x[-1]
                break

        return a
    def find_quick(s, tabel_name, kolonner, data, get = None):
        if get != None:
            if get not in s.column_names[tabel_name]:
                return False

        command = 'SELECT '

        #the column we want
        if(get != None):
            command += get + ' FROM ' + tabel_name
        else:
            command += '* FROM ' + tabel_name

        #conditions
        command += ' WHERE ' + kolonner[0] + ' = ?'
        if len(kolonner) > 1:
            for i in range(1, len(kolonner)):
                command += ' AND ' + kolonner[i] + ' = ?'

        print(command)
        c = s.con.cursor()
        c.execute(command, data)

        if get != None:
            for x in c:
                return x[0]
        else:
            for x in c:
                return True
        return False
    def find_with_links(s, linking_tabel, link_kolonner_1, link_kolonner_2, data, get = None, get_origin = None):
        #skal laves meget lig funktionen find, men tabeller skal linkes (det er hvad Søren ville kalde En-til-mange vi taler om her: http://bog.laerpython.dk/da/latest/ch-database/sqlite-advanced.html#en-til-mange-relation)

        #et eksempel kunne være i forhold til hvilke vagter der tilhørte hvilke ansatte.
        #linking_tabel kunne være 'VagtLink'
        #link_kolonner_1 kunne være ['VagtLink.PersonID', 'VagtLink.VagtID']
        #link_kolonner_1 kunne være ['Ansatte.ID', 'Vagt.ID']
        #data ville være noget som ['Peter', 124.4, 13]
        #get kunne være 'Kodeord' og get_origin kunne være 'Ansatte'
        pass
    def add_tabel(s, tabel_name, colums_names, colums_types):

        if tabel_name not in s.tabel_names:
            c = s.con.cursor()
            command = 'CREATE TABLE ' + str(tabel_name) + ' (ID INTERGER PRIMARY KEY,'
            for x in range(len(colums_names) - 1):
                command += colums_names[x] + ' ' + colums_types[x] + ','
            command += colums_names[-1] + ' ' + colums_types[-1] + ')'
            c.execute(command)
            s.tabel_names.append(tabel_name)
            s.column_names[tabel_name] = colums_names
            s.column_types[tabel_name] = colums_types

            s.column_names[tabel_name].insert(0, 'ID')
            s.column_types[tabel_name].insert(0, 'INT')
            s.con.commit()
        else:
            print('Har allerede tabellen ' + tabel_name + ' i databasen.')
    def insert(s, tabel_name, colum_names, data, index_column = None, index = None):
        if index != None:
            print(s.get_length(tabel_name))
            for i in range(s.get_length(tabel_name) - index + 1):
                s.edit(tabel_name, ID + i + 1, 'ID', ID + i + 2)

            command = 'INSERT INTO ' + tabel_name + '(ID'
            for x in range(len(colum_names) - 1):
                command += colum_names[x] + ','
            command += colum_names[-1] + ') VALUES (?'
            command += '?,' * (len(data) - 1) + '?)'
            data.insert(0, index)
            s.con.execute(command, data)
        else:
            command = 'INSERT INTO ' + tabel_name + '('
            for x in range(len(colum_names) - 1):
                command += colum_names[x] + ','
            command += colum_names[-1] + ') VALUES ('
            command += '?,' * (len(data) - 1) + '?)'
            s.con.execute(command, data)

        s.con.commit()
    def edit(s, tabel_name, ID, set_column, set_data):
        command = 'UPDATE ' + tabel_name + ' SET ' + set_column + ' = ? WHERE ID = ?'

        s.con.execute(command, [set_data, ID])
        s.con.commit()
    def find_and_edit(s, tabel_name, colum_names, data, set_column, set_data):
        command = 'UPDATE ' + tabel_name + ' SET ' + set_column + ' = ? WHERE ID = ?'

        s.con.execute(command, [set_data, s.find(tabel_name, column_names, data, get = 'ID')])
        s.con.commit()
    def remove(s, tabel_name, ID, edit_indexes = False):
        try:
            command = 'DELETE FROM ' + tabel_name + ' WHERE id = ' + str(ID)
            s.con.execute(command)

            if edit_indexes:
                for i in range(s.get_length(tabel_name) - ID + 1):
                    s.edit(tabel_name, ID + i + 1, 'ID', ID + i)

            s.con.commit()
            return True
        except:
            return False
    def find_and_remove(s, tabel_name, column_names, data, edit_indexes = False):
        try:
            command = 'DELETE FROM ' + tabel_name + ' WHERE id = ' + str(s.find(tabel_name, column_names, data, get = 'ID'))
            s.con.execute(command)
            s.con.commit()
            return True
        except:
            return False
    def get_length(s, tabel):
        c = s.con.cursor()
        c.execute('SELECT * FROM ' + tabel)
        count = 0
        for x in c:
            count += 1
        return count
    def print(s, tabel_name = None, show_ID = False):
        if len(s.tabel_names) == 0:
            print('Ingen tabeller')
            return
        c = s.con.cursor()

        largest_tabel = 0
        if tabel_name == None:
            for i in s.tabel_names:
                c.execute('SELECT * FROM ' + i)
                for j in c:
                    if len(j) > largest_tabel:
                        largest_tabel = len(j)
                    break
        else:
            c.execute('SELECT * FROM ' + tabel_name)
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

            for j in range(len(s.column_names[s.tabel_names[i]]) - 1):
                p += s.column_names[s.tabel_names[i]][j] + " | "
            p += s.column_names[s.tabel_names[i]][-1] + "\n"

            c.execute('SELECT * FROM ' + s.tabel_names[i])
            for j in c:
                for k in range(len(j) - 1):
                    p += str(j[k]) + " | "
                p += str(j[-1]) + "\n"
            p += "\n"

        t = math.floor(((largest_tabel * 3) - len(s.tabel_names[-1])) / 2 + 1)
        p += ('-' * t * 2) + s.tabel_names[-1] + ('-' * t * 2) + "\n"

        for j in range(len(s.column_names[s.tabel_names[-1]]) - 1):
            p += s.column_names[s.tabel_names[-1]][j] + " | "
        p += s.column_names[s.tabel_names[-1]][-1] + "\n"

        c.execute('SELECT * FROM ' + s.tabel_names[-1])
        for j in c:
            for k in range(len(j) - 1):
                p += str(j[k]) + " | "
            p += str(j[-1]) + "\n"

        p += "#" * 40 + '\n'

        return p

'''users_data = Data("users", columns = ['navn STRING', 'password STRING', 'rolle INT'], randoms = [['Joachim','1234', 14], ['Nicolai', '4321', 2], ['Michael', '1', 5], ['Alexander', '2', 6], ['Anders', '3', 9]])
users_data.print()

users_data.insert(["uwu","Peter Griffin"],["password","navn"])

print(users_data.find(["navn", "password"], ["Nicolai","4321"], get = 'peter'))'''



'''data1 = Data_Alternative()
data1.add_tabel("Katte", ['kat1', 'katte5'], ['STRING', 'INT'])
for x in range(3):
    data1.insert('Katte', ['kat1','katte5'], ['Joachim er bedre end Nicolai', 5])
data1.edit('Katte', 2, 'ID', 4)
data1.insert('Katte', ['kat1','katte5'], ['Nicolai er bedre end Nicolai', 5])
data1.print(tabel_name = 'Katte', show_ID = False)'''


'''data = Data_Alternative(
names = ["test_1", "test_2"],
column_names = [['col_1', 'col_2', 'col_3', 'col_4'],  ['trar', 'jiajwd']],
column_types = [['STRING', 'INT', 'INT', 'STRING'],  ['STRING', 'INT']],
defaults = [['lars', 5, 1, 'fem'], []],
not_nulls = [[None, None, None, True], [True, True, None, None]],
randoms = [[['peter', 5, 10, 'hej'], ['lars', 2000, 10, 'peter']], [['peter', 5], ['lars', 2000]]])
print(str(data))
data.remove('test_1', 1, edit_indexes = True)
print(str(data))'''
