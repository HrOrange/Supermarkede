#tkinter imports
import tkinter as tk

#generic imports
import time
import random
import math
import datetime
import enum

#from other files
import utility as util
import database

#ansatte_data = database.Data("Ansatte", columns = ['Navn STRING', 'Kodeord STRING', 'Løn REAL', 'Fyret INT', 'Rolle INT'], randoms = [['peter', 'hans', 4.5, 0, util.roller.butiks_chef.value], ['harry', 'klarry', 1200.2, 1, util.roller.butiks_chef.value], ['zahir', 'carl', -1, 0, util.roller.service_medarbejder.value]])
#ansatte_data.print()

users_data = database.Data("Kunder", columns = ['Navn STRING', 'Kodeord STRING'], randoms = [['Joachim','1234'], ['Nicolai', '4321'], ['Michael', '1'], ['Alexander', '2'], ['Anders', '3']])
#users_data.print()

'''ansatte_link_vagter = database.Data_Alternative(
names = ['Ansatte', 'VagtLink', 'Vagt'],
column_names = [['Navn', 'Kodeord', 'Løn', 'Fyret', 'Rolle'], ['PersonID', 'VagtID'], ['StartTid_Year', 'StartTid_Month', 'StartTid_Day', 'StartTid_Hour', 'StartTid_Minute', 'SlutTid_Year', 'SlutTid_Month', 'SlutTid_day', 'SlutTid_Hour', 'SlutTid_Minute', 'Uge_Dag']],
column_types = [['STRING', 'STRING', 'REAL', 'INT', 'INT'], ['INT', 'INT'], ['INT' for x in range(11)]],
randoms = [[['peter', 'hans', 4.5, 0, util.roller.butiks_chef.value], ['harry', 'klarry', 1200.2, 1, util.roller.butiks_chef.value], ['zahir', 'carl', -1, 0, util.roller.service_medarbejder.value]],
                   [[1, 1], [2, 2], [1, 3]],  #husk på at disse værdier er ID'er og ikke index værdier, hvilket vil sige at den ansatte ved navn peter har index værdi 0 og ID værdi 1.
                   [[2020, 5, 24, 12, 30, 2020, 24, 5, 16, 30, 5], [2020, 11, 10, 10, 30, 2021, 3, 25, 20, 30, 4], [2040, 11, 10, 10, 30, 2021, 3, 25, 20, 30, 3]]])'''

ansatte_vagter = database.Data_Alternative(
names = ['Ansatte', 'Vagt'],
column_names = [['Navn', 'Kodeord', 'Løn', 'Fyret', 'Rolle'], ['StartTid_Year', 'StartTid_Month', 'StartTid_Day', 'StartTid_Hour', 'StartTid_Minute', 'SlutTid_Year', 'SlutTid_Month', 'SlutTid_day', 'SlutTid_Hour', 'SlutTid_Minute', 'Uge_Dag', 'AnsatID']],
column_types = [['STRING', 'STRING', 'REAL', 'INT', 'INT'], ['INT' for x in range(12)]],
randoms = [[['peter', 'hans', 4.5, 0, util.roller.købmand.value], ['harry', 'klarry', 1200.2, 1, util.roller.butiks_chef.value], ['zahir', 'carl', -1, 0, util.roller.service_medarbejder.value]],
                   [[2020, 5, 24, 12, 30, 2020, 5, 24, 16, 30, datetime.date(2020, 5, 24).weekday(), 1], [2020, 11, 10, 10, 30, 2021, 3, 25, 20, 30, datetime.date(2020, 11, 10).weekday(), 3], [2040, 11, 10, 10, 30, 2021, 3, 25, 20, 30, datetime.date(2040, 11, 10).weekday(), 2], [2021, 2, 4, 10, 30, 2021, 2, 4, 20, 30, datetime.date(2021, 2, 4).weekday(), 2], [2021, 2, 6, 11, 0, 2021, 2, 6, 12, 30, datetime.date(2021, 2, 6).weekday(), 3]]])
print(str(ansatte_vagter))

'''printer de forskellige roller
counter = 1
for x in util.roller:
    print(str(counter) + ' : ' + str(x))
    counter += 1'''


#FONTS
#myFont = font.Font(family='Helvetica', size = 15, weight = "bold") old
myFont = ('Helvetica', '15', 'bold')
myBigFont = ('Helvetica', '20', 'bold')


##frames
class login_register_window(tk.Frame):
    def __init__(s, master = None, window_size = [300, 200], window_name = 'Login/Registrer', login = True):
        s.root = tk.Tk()
        tk.Frame.__init__(s, s.root)
        if s.root != None:
            s.root.title(window_name)

        s.closed = False

        #my_frame = tk.Frame(s, width = 300, height = 300)
        #my_frame.place(width=200, height=200)
        #s.root.protocol("WM_DELETE_WINDOW", lambda : s.root.destroy())

        s.root.geometry(str(window_size[0]) + 'x' + str(window_size[1]))
        s.place(width = window_size[0], height = window_size[1])
        #person information. Vi skulle måske lave en hel klasse til dette.
        s.navn = ''
        s.kodeord = ''
        s.rolle = 0

        #labels
        s.name_label = tk.Label(s, text = "Name", font = myFont)
        s.name_label.place(relx = 0.17, rely = 0.25, width = window_size[0] * 0.6, height = window_size[1] * 0.15, anchor = tk.CENTER)
        s.password_label = tk.Label(s, text = "Password", font = myFont)
        s.password_label.place(relx = 0.17, rely = 0.4, width = window_size[0] * 0.6, height = window_size[1] * 0.15, anchor = tk.CENTER)

        #entries
        s.name_entry = tk.Entry(s, font = myFont)
        s.name_entry.place(relx = 0.65, rely = 0.25, width = window_size[0] * 0.6, height = window_size[1] * 0.15, anchor = tk.CENTER)
        s.password_entry = tk.Entry(s, font = myFont)
        s.password_entry.place(relx = 0.65, rely = 0.4, width = window_size[0] * 0.6, height = window_size[1] * 0.15, anchor = tk.CENTER)

        #buttons
        button_size = [200, 50]
        s.login_button = tk.Button(s, text = "Login" if login == True else "Confirm", command = s.login if login == True else s.confirm_role, font = myFont)
        s.login_button.place(relx = 0.5, rely = 0.65, width = window_size[0] * 0.8, height = window_size[1] * 0.2, anchor = tk.CENTER)
        s.registrer_button = tk.Button(s, text="Registrer", command = s.registrer, font = myFont)
        s.registrer_button.place(relx = 0.5, rely = 0.85, width = window_size[0] * 0.8, height = window_size[1] * 0.2, anchor = tk.CENTER)

        s.mainloop()
    def confirm_role(s):
        if s.navn == '':
            name = s.name_entry.get()
            password = s.password_entry.get()

            #s.rolle = ansatte_data.find(['Navn', 'Kodeord'], [name, password], get = 'Rolle')
            s.rolle = ansatte_vagter.find('Ansatte', ['Navn', 'Kodeord'], [name, password], get = 'Rolle')
            s.close()
    def login(s):
        name = s.name_entry.get()
        password = s.password_entry.get()

        #ansat = ansatte_data.find(['Navn', 'Kodeord'], [name, password])
        ansat = ansatte_vagter.find('Ansatte', ['Navn', 'Kodeord'], [name, password])
        kunde = False
        if ansat == False:
            kunde = users_data.find(['Navn', 'Kodeord'], [name, password])

        if kunde or ansat:
            s.navn = name
            s.kodeord = password
            #s.rolle = ansatte_data.find(['Navn', 'Kodeord'], [name, password], get = 'Rolle')
            s.rolle = ansatte_vagter.find('Ansatte', ['Navn', 'Kodeord'], [name, password], get = 'Rolle')
            s.close()
        else:
            s.name_entry.delete(0, 'end')
            s.password_entry.delete(0, 'end')
            print('Navn eller kodeord er forkert')
    def registrer(s):
        name = s.name_entry.get()
        password = s.password_entry.get()

        #one way of doing this
        '''kunde_eller_ansat = yes_no_window(window_name = 'Vælg enten kunde eller ansat', button_texts = ['Kunde', 'Ansat'])

        findes_i_database = False
        if kunde_eller_ansat.answer == 'Ansat':
            findes_i_database = ansatte_vagter.find('Ansatte', ['Navn', 'Kodeord'], [name, password])
        elif kunde_eller_ansat.answer == 'Kunde':
            findes_i_database = users_data.find(['Navn', 'Kodeord'], [name, password])'''

        findes_i_database = ansatte_vagter.find('Ansatte', ['Navn', 'Kodeord'], [name, password])
        if findes_i_database == False:
            findes_i_database = users_data.find(['Navn', 'Kodeord'], [name, password])

        if findes_i_database:
            s.name_entry.delete(0, tk.END)
            s.password_entry.delete(0, tk.END)
            print('Navn eller kodeord bruges allerede')
        else:
            s.navn = name
            s.kodeord = password
            '''if kunde_eller_ansat.answer == 'Ansat':
                s.rolle = util.roller.ansat.value
                ansatte_vagter.insert('Ansatte', ['Navn', 'Kodeord', 'Rolle'], [s.navn, s.kodeord, util.roller.kunde.value])
            else:
                s.rolle = util.roller.kunde.value
                users_data.insert(s.navn, s.kodeord)'''
            s.rolle = util.roller.kunde.value
            users_data.insert([s.navn, s.kodeord], ['Navn', 'Kodeord'])
            s.close()
    def close(s):
        s.root.destroy()
        s.closed = True
class ansat_window(tk.Frame):
    def __init__(s, master = None, window_size = [600, 400], window_name = 'Ansat konsol'):
        s.root = tk.Tk()
        #s.root.geometry(str(window_size[0]) + "x" + str(window_size[1])) i denne classes bruges der pack, så størrelsen på root sættes automatisk
        tk.Frame.__init__(s, s.root)
        s.pack()
        #s.place(width = window_size[0], height = window_size[1]) i denne classes bruges der pack, så størrelsen på root sættes automatisk
        if s.root != None:
            s.root.title(window_name)
        #s.bind('<Configure>', window_resize_event) #this calls the function window_resize_event whenever a window resize event is happening

        #frames
        s.right_frame = tk.Frame(s, bg = 'red', width = window_size[0] * 0.6, height = window_size[1])
        s.left_frame = tk.Frame(s, bg = 'blue', width = window_size[0] * 0.4, height = window_size[1])
        s.top_right_frame = tk.Frame(s.right_frame, bg = 'pink', width = window_size[0] * 0.6, height = window_size[1] * 0.6)
        s.bottom_right_frame = tk.Frame(s.right_frame, bg = 'orange', width = window_size[0] * 0.6, height = window_size[1] * 0.4)

        s.left_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        s.right_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        s.bottom_right_frame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        s.top_right_frame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)

        #buttons

        s.buttons = {}
        variable_names = ['edit_price_button', 'profile']
        texts = ['Rediger Pris', 'Profil']
        funcs = [s.edit_price, s.profile_window]
        if login_window.rolle > util.roller.kunde.value:
            variable_names.insert(len(variable_names) - 1, 'shift_button')
            texts.insert(len(texts) - 1, 'Vagter')
            funcs.insert(len(funcs) - 1, s.shift_window)

            variable_names.insert(len(variable_names) - 1, 'role_button')
            texts.insert(len(texts) - 1, 'Roller')
            funcs.insert(len(funcs) - 1, s.role_window)

        if login_window.rolle >= util.roller.lukke_ansvarlig.value:
            pass #Kan ikke på nuværende tidspunkt nævne hvilke vinduer der skulle være tilgængelig for en lukke_ansvarlig eller højere

        for i in range(len(texts)):
            s.buttons[variable_names[i]] = tk.Button(s.left_frame, text = texts[i], command = funcs[i], font = myFont)
            #s.buttons[variable_names[i]].place(relx = 0.5, rely = (i + 0.5) / len(texts), relwidth = 1, relheight = 1 / len(texts), anchor = tk.CENTER)
            s.buttons[variable_names[i]].pack(expand = True, fill = tk.BOTH)

        #this is the same as above, just you know, more boring and hardcoded
        #s.give_role_button = tk.Button(left_frame, text = "Giv Rolle", command = give_role).pack(side = tk.TOP)
        #s.edit_role_button = tk.Button(left_frame, text = "Rediger Rolle", command = edit_role).pack(side = tk.TOP)
        #s.edit_price_button = tk.Button(left_frame, text = "Rediger Pris", command = edit_pris).pack(side = tk.TOP)
        #s.shift_overview_button = tk.Button(left_frame, text = "Vagt Oversigt", command = shift_overview).pack(side = tk.TOP)

        s.windows = {'role_window' : {'window' : None, 'opened' : None},
                              'shift_window' : {'window' : None, 'opened' : None},
                              'profile_window' : {'window' : None, 'opened' : None}}
        s.mainloop()
    def edit_price(s):
        #TODO: open toplevel
        pass

    def role_window(s):
        if s.windows['role_window']['opened'] == None:
            s.windows['role_window']['opened'] = role_overall_window()
        elif s.windows['role_window']['opened'].closed:
            s.windows['role_window']['opened'] = role_overall_window()
    def shift_window(s):
        if s.windows['shift_window']['opened'] == None:
            s.windows['shift_window']['opened'] = shift_overall_window()
        elif s.windows['shift_window']['opened'].closed:
            s.windows['shift_window']['opened'] = shift_overall_window()
    def profile_window(s):
        if s.windows['profile_window']['opened'] == None:
            s.windows['profile_window']['opened'] = profile_window()
        elif s.windows['profile_window']['opened'].closed:
            s.windows['profile_window']['opened'] = profile_window()
    def window_resize_event(s, event):
        size = int(20 * (0.4 * s.root.winfo_width() / originial_window_size[0] + 0.6 * s.root.winfo_height() / originial_window_size[1]))
        for i in buttons:
            s.buttons[i]['font'] = s.myFont
    def close(s):
        s.root.destroy()
class kunde_window(tk.Frame):
    def __init__(s, master = None, window_size = [600, 400], window_name = 'Kunde Hjem'):
        s.root = tk.Tk()
        #s.root.geometry(str(window_size[0]) + "x" + str(window_size[1])) i denne classes bruges der pack, så størrelsen på root sættes automatisk
        tk.Frame.__init__(s, s.root)
        s.pack()
        #s.place(width = window_size[0], height = window_size[1]) i denne classes bruges der pack, så størrelsen på root sættes automatisk
        if s.root != None:
            s.root.title(window_name)
        #s.bind('<Configure>', window_resize_event) #this calls the function window_resize_event whenever a window resize event is happening

        #frames
        s.right_frame = tk.Frame(s, bg = 'red', width = window_size[0] * 0.6, height = window_size[1])
        s.left_frame = tk.Frame(s, bg = 'blue', width = window_size[0] * 0.4, height = window_size[1])
        s.top_right_frame = tk.Frame(s.right_frame, bg = 'pink', width = window_size[0] * 0.6, height = window_size[1] * 0.6)
        s.bottom_right_frame = tk.Frame(s.right_frame, bg = 'orange', width = window_size[0] * 0.6, height = window_size[1] * 0.4)

        s.left_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        s.right_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        s.bottom_right_frame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
        s.top_right_frame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)

        #buttons

        s.buttons = {}
        variable_names = ['profile']
        texts = ['Profil']
        funcs = [s.profile_window]

        for i in range(len(texts)):
            s.buttons[variable_names[i]] = tk.Button(s.left_frame, text = texts[i], command = funcs[i], font = myFont)
            #s.buttons[variable_names[i]].place(relx = 0.5, rely = (i + 0.5) / len(texts), relwidth = 1, relheight = 1 / len(texts), anchor = tk.CENTER)
            s.buttons[variable_names[i]].pack(expand = True, fill = tk.BOTH)

        #this is the same as above, just you know, more boring and hardcoded
        #s.give_role_button = tk.Button(left_frame, text = "Giv Rolle", command = give_role).pack(side = tk.TOP)
        #s.edit_role_button = tk.Button(left_frame, text = "Rediger Rolle", command = edit_role).pack(side = tk.TOP)
        #s.edit_price_button = tk.Button(left_frame, text = "Rediger Pris", command = edit_pris).pack(side = tk.TOP)
        #s.shift_overview_button = tk.Button(left_frame, text = "Vagt Oversigt", command = shift_overview).pack(side = tk.TOP)

        s.windows = {'profile_window' : {'window' : None, 'opened' : None}}
        s.mainloop()
    def profile_window(s):
        if s.windows['profile_window']['opened'] == None:
            s.windows['profile_window']['opened'] = profile_window()
        elif s.windows['profile_window']['opened'].closed:
            s.windows['profile_window']['opened'] = profile_window()
    def window_resize_event(s, event):
        size = int(20 * (0.4 * s.root.winfo_width() / originial_window_size[0] + 0.6 * s.root.winfo_height() / originial_window_size[1]))
        for i in buttons:
            s.buttons[i]['font'] = s.myFont
    def close(s):
        s.root.destroy()
class yes_no_window(tk.Frame):
    def __init__(s, master = None, window_name = 'Click Ja eller Nej', button_texts = ['Ja', 'Nej'], window_size = [300, 100]):
        s.root = tk.Tk()
        tk.Frame.__init__(s, s.root)
        if s.root != None:
            s.root.title(window_name)
        s.root.geometry(str(window_size[0]) + 'x' + str(window_size[1]))
        s.place(width = window_size[0], height = window_size[1])
        s.closed = False
        s.button_texts = button_texts

        s.answer = button_texts[1]

        s.yes_button = tk.Button(s.root, text = button_texts[0], command = s.yes, font = myBigFont)
        s.yes_button.place(relx = 0.25, rely = 0.5, relwidth = 0.4, relheight = 0.4, anchor = tk.CENTER)

        s.no_button = tk.Button(s.root, text = button_texts[1], command = s.no, font = myBigFont)
        s.no_button.place(relx = 0.75, rely = 0.5, relwidth = 0.4, relheight = 0.4, anchor = tk.CENTER)

        s.mainloop()
    def yes(s):
        s.answer = s.button_texts[0]
        s.close()
    def no(s):
        s.close()
    def close(s):
        s.root.quit()
        s.root.destroy()
        s.closed = True

##toplevels
#shift
class shift_overall_window:
    def __init__(s, toplevel_size = [500, 400], window_name = 'Vagter'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.buttons = {}
        button_names = ['shift_overview_open']
        button_funcs = [s.shift_overview_open]
        button_texts = ['Vagt Oversigt']

        if login_window.rolle >= util.roller.lukke_ansvarlig.value:
            button_names.insert(len(button_names) - 1, 'add_shift')
            button_funcs.insert(len(button_funcs) - 1, s.add_shift)
            button_texts.insert(len(button_texts) - 1, 'Tilføj Vagt')

            button_names.insert(len(button_names) - 1, 'remove_shift')
            button_funcs.insert(len(button_funcs) - 1, s.remove_shift)
            button_texts.insert(len(button_texts) - 1, 'Fjern Vagt')

            button_names.insert(len(button_names) - 1, 'edit_shift')
            button_funcs.insert(len(button_funcs) - 1, s.edit_shift)
            button_texts.insert(len(button_texts) - 1, 'Rediger Vagt')

        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.root, text = button_texts[i], command = button_funcs[i], font = myFont).pack(fill = tk.X), 'opened' : None}

    def shift_overview_open(s):
        if s.buttons['shift_overview_open']['opened'] == None:
            s.buttons['shift_overview_open']['opened'] = shift_overview_window()
        elif s.buttons['shift_overview_open']['opened'].closed:
            s.buttons['shift_overview_open']['opened'] = shift_overview_window()
    def add_shift(s):
        if s.buttons['add_shift']['opened'] == None:
            s.buttons['add_shift']['opened'] = add_shift_window()
        elif s.buttons['add_shift']['opened'].closed:
            s.buttons['add_shift']['opened'] = add_shift_window()
    def remove_shift(s):
        if s.buttons['remove_shift']['opened'] == None:
            s.buttons['remove_shift']['opened'] = remove_shift_window()
        elif s.buttons['remove_shift']['opened'].closed:
            s.buttons['remove_shift']['opened'] = remove_shift_window()
    def edit_shift(s):
        if s.buttons['edit_shift']['opened'] == None:
            s.buttons['edit_shift']['opened'] = shift_overview_window()
        elif s.buttons['edit_shift']['opened'].closed:
            s.buttons['edit_shift']['opened'] = shift_overview_window()
class shift_overview_window:

    def __init__(s, toplevel_size = [500, 400], window_name = 'Vagt oversigt'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.closed = False
        s.root.protocol("WM_DELETE_WINDOW", s.close)
        ##first create the scrollbar
        #scroll_bar = tk.Scrollbar(s.root)
        ##then create the content within
        #can = tk.Canvas(s.root, yscrollcommand = scroll_bar.set)
        #scroll_bar.grid(row = 0, column = 8, rowspan = 4)
        s.week_add = 0

        s.right_button_image = tk.PhotoImage(file = "billeder/right.png").subsample(8, 8)
        s.left_button_image = tk.PhotoImage(file = "billeder/left.png").subsample(8, 8)
        s.left_button = tk.Button(s.root, text = '', command = s.left, width = 40, height = 40, image = s.left_button_image)
        s.left_button.grid(row = 0, column = 0)
        s.middle_label = tk.Label(s.root, text = 'Uge', font = myFont)
        s.middle_label.grid(row = 0, column = 1)
        s.right_button = tk.Button(s.root, text = '', command = s.right, width = 40, height = 40, image = s.right_button_image)
        s.right_button.grid(row = 0, column = 2)

        today = datetime.datetime.now().strftime("%Y/%m/%d/%H/%M/%S").split('/')
        current_year = int(today[0])
        current_month = int(today[1])
        current_day = int(today[2])
        current_hour = int(today[3])
        current_minute = int(today[4])
        current_second = int(today[5])
        week_number = datetime.date(current_year, current_month, current_day).isocalendar()[1]
        current_week_day = datetime.datetime.today().weekday()

        s.tabel = [[]] #række, kolonne
        kolonne_titler = ['Uge ' + str(week_number), 'Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredage', 'Lørdag', 'Søndag']
        for i in range(len(kolonne_titler)):
            s.tabel[0].append(tk.Entry(s.root , font = myFont, justify = 'center', width = 15))
            s.tabel[-1][-1].insert(tk.END, kolonne_titler[i])
            s.tabel[-1][-1].grid(row = 1, column = i)


        #c = ansatte_vagter.find_with_links('VagtLink', ['Navn', '', 'StartTid_Day'])
        c = ansatte_vagter.con.cursor()
        c.execute('''SELECT Ansatte.Navn, Vagt.StartTid_Year, Vagt.StartTid_Month, Vagt.StartTid_Day, Vagt.StartTid_Hour, Vagt.StartTid_Minute, Vagt.SlutTid_Year, Vagt.SlutTid_Month, Vagt.SlutTid_Day, Vagt.SlutTid_Hour, Vagt.SlutTid_Minute, Vagt.Uge_Dag, Vagt.AnsatID
        FROM Vagt
        INNER JOIN Ansatte
        ON Vagt.AnsatID = Ansatte.ID''')
        antal_ansatte = ansatte_vagter.get_length('Ansatte')
        for i in range(antal_ansatte):
            s.tabel.append([])
            for j in range(8):
                s.tabel[-1].append(tk.Entry(s.root, font = myFont, justify = 'center', width = 15))
                s.tabel[-1][-1].grid(row = i + 2, column = j)

        c_2 = ansatte_vagter.con.cursor()
        c_2.execute('SELECT Navn FROM Ansatte')
        count = 1
        for x in c_2:
            s.tabel[count][0].insert(tk.END, x[0])
            count += 1

        for x in c:
            if x[11] == week_number and x[1] == current_year:
                s.tabel[x[12]][datetime.date(x[1], x[2], x[3]).weekday() + 1].insert(tk.END, str(x[4]) + ':' + str(x[5]) + ' - ' + str(x[9]) + ':' + str(x[10]))

        for i in range(len(s.tabel)):
            for j in range(len(s.tabel[i])):
                s.tabel[i][j].config(state = 'disabled')

        #diskuter denne knap med gruppen. Den knap skal kun være tilgængelig for folk der er butiks_chef eller højere.
        #apply_button = tk.Button(s.root, font = myFont, text = 'Apply', command = s.apply_change)
        #apply_button.grid(row = antal_ansatte + 1, column = 7)
        ''' canvas approse
        s.cat = tk.Canvas(s.root, height = toplevel_size[0], width = toplevel_size[1], bg='white')
        s.cat.pack(fill = tk.BOTH, expand = True)

        offX = int(toplevel_size[0] / 7)
        for i in range(0, toplevel_size[0], offX):
            s.cat.create_line([(i, 0), (i, toplevel_size[1])])

        offY = int(toplevel_size[1] / 5)
        for i in range(0, toplevel_size[1], offY):
            s.cat.create_line([(0, i), (toplevel_size[0], i)])'''
    def right(s):
        s.week_add += 1
        s.update_week_box()

    def left(s):
        s.week_add -= 1
        s.update_week_box()

    def update_week_box(s):
        today = datetime.datetime.now().strftime("%Y/%m/%d/%H/%M/%S").split('/')
        current_year = int(today[0])
        current_month = int(today[1])
        current_day = int(today[2])
        week_number = datetime.date(current_year, current_month, current_day).isocalendar()[1] + s.week_add
        if week_number > 52:
            while week_number > 52:
                week_number -= 52
                current_year += 1
        elif week_number <= 0:
            while week_number < 0:
                week_number += 52
                current_year -= 1

        for i in range(len(s.tabel)):
            for j in range(len(s.tabel[i])):
                s.tabel[i][j].config(state = 'normal')

        s.tabel[0][0].delete(0, tk.END)
        s.tabel[0][0].insert(0, 'Uge ' + str(week_number))

        antal_ansatte = ansatte_vagter.get_length('Ansatte')
        for i in range(antal_ansatte):
            for j in range(1, 8):
                s.tabel[i + 1][j].delete(0, tk.END)

        c = ansatte_vagter.con.cursor()
        c.execute('''SELECT Ansatte.Navn, Vagt.StartTid_Year, Vagt.StartTid_Month, Vagt.StartTid_Day, Vagt.StartTid_Hour, Vagt.StartTid_Minute, Vagt.SlutTid_Year, Vagt.SlutTid_Month, Vagt.SlutTid_Day, Vagt.SlutTid_Hour, Vagt.SlutTid_Minute, Vagt.Uge_Dag, Vagt.AnsatID
        FROM Vagt
        INNER JOIN Ansatte
        ON Vagt.AnsatID = Ansatte.ID''')

        for x in c:
            if x[11] == week_number and x[1] == current_year:
                w = datetime.date(x[1], x[2], x[3]).weekday() + 1
                s.tabel[x[12]][w].insert(0, str(x[4]) + ':' + str(x[5]) + ' - ' + str(x[9]) + ':' + str(x[10]))

        for i in range(len(s.tabel)):
            for j in range(len(s.tabel[i])):
                s.tabel[i][j].config(state = 'disabled')

    def close(s):
        s.closed = True
        s.root.destroy()
class add_shift_window:
    def __init__(s, toplevel_size = [500, 400], window_name = 'Tilføj vagt'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.closed = False
        s.root.protocol("WM_DELETE_WINDOW", s.close)

        #Ansattes navn
        s.name_label = tk.Label(s.root, text = "Navn", font = myFont)
        s.name_label.grid(row = 0, column = 0)

        s.dropdown_name_var = tk.StringVar(s.root)
        s.dropdown_name_options = []
        c = ansatte_vagter.con.cursor()
        c.execute('SELECT Navn FROM Ansatte')
        for x in c:
            s.dropdown_name_options.append(x[0])
        s.dropdown_name_var.set(s.dropdown_name_options[0]) # default value

        s.dropdown_name = tk.OptionMenu(s.root, s.dropdown_name_var, *s.dropdown_name_options)
        s.dropdown_name.config(font = myFont)
        s.dropdown_name.grid(row = 0, column = 1)

        #Tidsrummet
        s.dato_label = tk.Label(s.root, text = "Dato (dd.mm)", font = myFont)
        s.dato_label.grid(row = 1, column = 0)

        s.dato_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.dato_entry.grid(row = 1, column = 1)

        s.start_label = tk.Label(s.root, text = "Start Tidspunkt (HH:MM)", font = myFont)
        s.start_label.grid(row = 2, column = 0)

        s.start_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.start_entry.grid(row = 2, column = 1)

        s.slut_label = tk.Label(s.root, text = "Slut Tidspunkt (HH:MM)", font = myFont)
        s.slut_label.grid(row = 3, column = 0)

        s.slut_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.slut_entry.grid(row = 3, column = 1)


        #buttons in bottom
        button_names = ['add_shift', 'cancel']
        button_funcs = [s.add_shift, s.close]
        button_texts = ['Tilføj Vagt', 'Afbryd']
        s.buttons = {}
        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.root, text = button_texts[i], command = button_funcs[i], font = myFont).grid(row = 4, column = i), 'opened' : None}

    def add_shift(s):
        start = s.start_entry.get().split(':')
        slut = s.slut_entry.get().split(':')
        dato = s.dato_entry.get().split('.')
        name = s.dropdown_name_var.get()

        if len(start) != 2 or len(slut) != 2 or len(dato) != 2:
            if len(start) != 2:
                s.start_entry.delete(0, tk.END)
            if len(slut) != 2:
                s.slut_entry.delete(0, tk.END)
            if len(dato) != 2:
                s.dato_entry.delete(0, tk.END)
        else:
            try:
                start_hour = int(start[0])
                start_minute = int(start[1])
                slut_hour = int(slut[0])
                slut_minute = int(slut[1])
                dag = int(dato[0])
                månede = int(dato[1])

                today = datetime.datetime.now().strftime("%Y/%m/%d/%H/%M/%S").split('/')
                current_year = int(today[0])
                current_month = int(today[1])
                current_day = int(today[2])
                current_hour = int(today[3])
                current_minute = int(today[4])
                current_second = int(today[5])
                week_number = datetime.date(current_year, current_month, current_day).isocalendar()[1]

                slut_dag = dag
                slut_månede = månede
                if current_month > månede:
                    current_year += 1 #jeg antager at man ikke kan få et vagt som foregår i to år på samme tid.
                if start_hour > slut_hour:
                    slut_dag += 1 #jeg antager at hvis man vælger f.eks. kl 22 som start_hour og 04 som slut_hour, så foregår vagten over to dage
                if start_hour > slut_hour or start_hour == slut_hour and start_minute > slut_minute:
                    start_hour, slut_hour = util.swap(start_hour, slut_hour)

                id = ansatte_vagter.find('Ansatte', ['Navn'], [name], get = 'ID')
                if ansatte_vagter.find('Vagt', ['StartTid_Year', 'StartTid_Month', 'StartTid_Day', 'AnsatID'], [current_year, current_month, dag, id]) == False:
                    print('Tilføjer vagt for: ' + name + ' med start tidspunkt på: ' + s.start_entry.get() + ' og med slut tidspunkt på: ' + s.slut_entry.get())
                    ansatte_vagter.insert('Vagt',
                    ['StartTid_Year, StartTid_Month, StartTid_Day, StartTid_Hour, StartTid_Minute', 'SlutTid_Year, SlutTid_Month, SlutTid_Day, SlutTid_Hour, SlutTid_Minute', 'Uge_Dag', 'AnsatID'],
                    [current_year, current_month, dag, start_hour, start_minute, current_year, current_month, slut_dag, slut_hour, slut_minute, datetime.date(current_year, månede, dag).isocalendar()[1], id])
                    print([current_year, current_month, dag, start_hour, start_minute, current_year, current_month, slut_dag, slut_hour, slut_minute, datetime.date(current_year, månede, dag).isocalendar()[1], id])

                s.close()
            except:
                s.start_entry.delete(0, tk.END)
                s.slut_entry.delete(0, tk.END)
                s.dato_entry.delete(0, tk.END)
    def close(s):
        s.closed = True
        s.root.destroy()
class remove_shift_window:
    def __init__(s, toplevel_size = [500, 400], window_name = 'Fjern vagt'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.closed = False
        s.root.protocol("WM_DELETE_WINDOW", s.close)

        #Ansattes navn
        s.name_label = tk.Label(s.root, text = "Navn", font = myFont)
        s.name_label.grid(row = 0, column = 0)

        s.dropdown_name_var = tk.StringVar(s.root)
        s.dropdown_name_options = []
        c = ansatte_vagter.con.cursor()
        c.execute('SELECT Navn FROM Ansatte')
        for x in c:
            s.dropdown_name_options.append(x[0])
        s.dropdown_name_var.set(s.dropdown_name_options[0]) # default value

        s.dropdown_name = tk.OptionMenu(s.root, s.dropdown_name_var, *s.dropdown_name_options)
        s.dropdown_name.config(font = myFont)
        s.dropdown_name.grid(row = 0, column = 1)

        #Tidsrummet
        s.dato_label = tk.Label(s.root, text = "Dato (dd.mm)", font = myFont)
        s.dato_label.grid(row = 1, column = 0)

        s.dato_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.dato_entry.grid(row = 1, column = 1)


        #buttons in bottom
        button_names = ['remove_shift', 'cancel']
        button_funcs = [s.remove_shift, s.close]
        button_texts = ['Fjern Vagt', 'Afbryd']
        s.buttons = {}
        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.root, text = button_texts[i], command = button_funcs[i], font = myFont).grid(row = 2, column = i), 'opened' : None}

    def remove_shift(s):
        dato = s.dato_entry.get().split('.')
        name = s.dropdown_name_var.get()

        if len(dato) != 2:
            s.dato_entry.delete(0, tk.END)
        else:
            try:
                dag = int(dato[0])
                månede = int(dato[1])

                ansat_id = ansatte_vagter.find('Ansatte', ['Navn'], [name], get = 'ID')
                vagt_id = ansatte_vagter.find('Vagt', ['AnsatID', 'StartTid_Month', 'StartTid_Day'], [ansat_id, månede, dag], get = 'ID')
                if vagt_id != False:
                    print('Fjerner en vagt for ' + name + ' den ' + str(dag) + "." + str(månede))
                    success = ansatte_vagter.remove('Vagt', vagt_id, edit_indexes = True)
                    if success:
                        print('havde success med at fjerne vagt fra ' + name)
                    else:
                        print(name + ' har ikke en vagt på den dato.')

                s.close()
            except:
                s.dato_entry.delete(0, tk.END)
    def close(s):
        s.closed = True
        s.root.destroy()

#vare (ikke begyndt)
class product_overall_window:
    def __init__(s, toplevel_size = [500, 400], window_name = 'Vagter'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        button_names = ['shift_overview_open', 'add_shift', 'remove_shift', 'edit_shift']
        button_funcs = [s.shift_overview_open, s.add_shift, s.remove_shift, s.edit_shift]
        button_texts = ['Vagt Oversigt', 'Tilføj Vagt', 'Fjern Vagt', 'Rediger Vagt']
        s.buttons = {}
        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.root, text = button_texts[i], command = button_funcs[i], font = myFont).pack(fill = tk.X), 'opened' : None}

    def shift_overview_open(s):
        if s.buttons['shift_overview_open']['opened'] == None:
            s.buttons['shift_overview_open']['opened'] = shift_overview_window()
        elif s.buttons['shift_overview_open']['opened'].closed:
            s.buttons['shift_overview_open']['opened'] = shift_overview_window()
    def add_shift(s):
        if s.buttons['add_shift']['opened'] == None:
            s.buttons['add_shift']['opened'] = add_shift_window()
        elif s.buttons['add_shift']['opened'].closed:
            s.buttons['add_shift']['opened'] = add_shift_window()
    def remove_shift(s):
        if s.buttons['remove_shift']['opened'] == None:
            s.buttons['remove_shift']['opened'] = remove_shift_window()
        elif s.buttons['remove_shift']['opened'].closed:
            s.buttons['remove_shift']['opened'] = remove_shift_window()
    def edit_shift(s):
        if s.buttons['edit_shift']['opened'] == None:
            s.buttons['edit_shift']['opened'] = shift_overview_window()
        elif s.buttons['edit_shift']['opened'].closed:
            s.buttons['edit_shift']['opened'] = shift_overview_window()
class product_overview_window:

    def __init__(s, toplevel_size = [500, 400], window_name = 'Vagt oversigt'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.closed = False
        s.root.protocol("WM_DELETE_WINDOW", s.close)
        ##first create the scrollbar
        #scroll_bar = tk.Scrollbar(s.root)
        ##then create the content within
        #can = tk.Canvas(s.root, yscrollcommand = scroll_bar.set)
        #scroll_bar.grid(row = 0, column = 8, rowspan = 4)


        today = datetime.datetime.now().strftime("%Y/%m/%d/%H/%M/%S").split('/')
        current_year = int(today[0])
        current_month = int(today[1])
        current_day = int(today[2])
        current_hour = int(today[3])
        current_minute = int(today[4])
        current_second = int(today[5])
        week_number = datetime.date(current_year, current_month, current_day).isocalendar()[1]
        current_week_day = datetime.datetime.today().weekday()

        s.tabel = [[]] #række, kolonne
        kolonne_titler = ['Uge ' + str(week_number), 'Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredage', 'Lørdag', 'Søndag']
        for i in range(len(kolonne_titler)):
            s.tabel[0].append(tk.Entry(s.root , font = myFont, justify = 'center'))
            s.tabel[-1][-1].insert(tk.END, kolonne_titler[i])
            s.tabel[-1][-1].grid(row = 0, column = i)


        #c = ansatte_vagter.find_with_links('VagtLink', ['Navn', '', 'StartTid_Day'])
        c = ansatte_vagter.con.cursor()
        c.execute('''SELECT Ansatte.Navn, Vagt.StartTid_Year, Vagt.StartTid_Month, Vagt.StartTid_Day, Vagt.StartTid_Hour, Vagt.StartTid_Minute, Vagt.SlutTid_Year, Vagt.SlutTid_Month, Vagt.SlutTid_Day, Vagt.SlutTid_Hour, Vagt.SlutTid_Minute, Vagt.Uge_Dag, Vagt.AnsatID
        FROM Vagt
        INNER JOIN Ansatte
        ON Vagt.AnsatID = Ansatte.ID''')
        antal_ansatte = ansatte_vagter.get_length('Ansatte')
        for i in range(antal_ansatte):
            s.tabel.append([])
            for j in range(8):
                s.tabel[-1].append(tk.Entry(s.root, font = myFont, justify = 'center'))
                s.tabel[-1][-1].grid(row = i + 1, column = j)

        c_2 = ansatte_vagter.con.cursor()
        c_2.execute('SELECT Navn FROM Ansatte')
        count = 1
        for x in c_2:
            s.tabel[count][0].insert(tk.END, x[0])
            count += 1

        count = 0
        for x in c:
            if x[11] == week_number and x[1] == current_year:
                s.tabel[x[12]][datetime.date(x[1], x[2], x[3]).weekday() + 1].insert(tk.END, str(x[4]) + ':' + str(x[5]) + ' - ' + str(x[9]) + ':' + str(x[10]))

        for i in range(len(s.tabel)):
            for j in range(len(s.tabel[i])):
                s.tabel[i][j].config(state = 'disabled')

        #diskuter denne knap med gruppen. Den knap skal kun være tilgængelig for folk der er butiks_chef eller højere.
        #apply_button = tk.Button(s.root, font = myFont, text = 'Apply', command = s.apply_change)
        #apply_button.grid(row = antal_ansatte + 1, column = 7)
        ''' canvas approse
        s.cat = tk.Canvas(s.root, height = toplevel_size[0], width = toplevel_size[1], bg='white')
        s.cat.pack(fill = tk.BOTH, expand = True)

        offX = int(toplevel_size[0] / 7)
        for i in range(0, toplevel_size[0], offX):
            s.cat.create_line([(i, 0), (i, toplevel_size[1])])

        offY = int(toplevel_size[1] / 5)
        for i in range(0, toplevel_size[1], offY):
            s.cat.create_line([(0, i), (toplevel_size[0], i)])'''
    def apply_change(s):
        print('Hello')
    def close(s):
        s.closed = True
        s.root.destroy()
class add_product_window:
    def __init__(s, toplevel_size = [500, 400], window_name = 'Tilføj vagt'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.closed = False
        s.root.protocol("WM_DELETE_WINDOW", s.close)

        #Ansattes navn
        s.name_label = tk.Label(s.root, text = "Navn", font = myFont)
        s.name_label.grid(row = 0, column = 0)

        s.dropdown_name_var = tk.StringVar(s.root)
        s.dropdown_name_options = []
        c = ansatte_vagter.con.cursor()
        c.execute('SELECT Navn FROM Ansatte')
        for x in c:
            s.dropdown_name_options.append(x[0])
        s.dropdown_name_var.set(s.dropdown_name_options[0]) # default value

        s.dropdown_name = tk.OptionMenu(s.root, s.dropdown_name_var, *s.dropdown_name_options)
        s.dropdown_name.config(font = myFont)
        s.dropdown_name.grid(row = 0, column = 1)

        #Tidsrummet
        s.dato_label = tk.Label(s.root, text = "Dato (dd.mm)", font = myFont)
        s.dato_label.grid(row = 1, column = 0)

        s.dato_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.dato_entry.grid(row = 1, column = 1)

        s.start_label = tk.Label(s.root, text = "Start Tidspunkt (HH:MM)", font = myFont)
        s.start_label.grid(row = 2, column = 0)

        s.start_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.start_entry.grid(row = 2, column = 1)

        s.slut_label = tk.Label(s.root, text = "Slut Tidspunkt (HH:MM)", font = myFont)
        s.slut_label.grid(row = 3, column = 0)

        s.slut_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.slut_entry.grid(row = 3, column = 1)


        #buttons in bottom
        button_names = ['add_shift', 'cancel']
        button_funcs = [s.add_shift, s.close]
        button_texts = ['Tilføj Vagt', 'Afbryd']
        s.buttons = {}
        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.root, text = button_texts[i], command = button_funcs[i], font = myFont).grid(row = 4, column = i), 'opened' : None}

    def add_shift(s):
        start = s.start_entry.get().split(':')
        slut = s.slut_entry.get().split(':')
        dato = s.dato_entry.get().split('.')
        name = s.dropdown_name_var.get()

        if len(start) != 2 or len(slut) != 2 or len(dato) != 2:
            if len(start) != 2:
                s.start_entry.delete(0, tk.END)
            if len(slut) != 2:
                s.slut_entry.delete(0, tk.END)
            if len(dato) != 2:
                s.dato_entry.delete(0, tk.END)
        else:
            try:
                start_hour = int(start[0])
                start_minute = int(start[1])
                slut_hour = int(slut[0])
                slut_minute = int(slut[1])
                dag = int(dato[0])
                månede = int(dato[1])

                today = datetime.datetime.now().strftime("%Y/%m/%d/%H/%M/%S").split('/')
                current_year = int(today[0])
                current_month = int(today[1])
                current_day = int(today[2])
                current_hour = int(today[3])
                current_minute = int(today[4])
                current_second = int(today[5])
                week_number = datetime.date(current_year, current_month, current_day).isocalendar()[1]

                slut_dag = dag
                slut_månede = månede
                if current_month > månede:
                    current_year += 1 #jeg antager at man ikke kan få et vagt som foregår i to år på samme tid.
                if start_hour > slut_hour:
                    slut_dag += 1 #jeg antager at hvis man vælger f.eks. kl 22 som start_hour og 04 som slut_hour, så foregår vagten over to dage
                if start_hour > slut_hour or start_hour == slut_hour and start_minute > slut_minute:
                    start_hour, slut_hour = util.swap(start_hour, slut_hour)

                id = ansatte_vagter.find('Ansatte', ['Navn'], [name], get = 'ID')
                if ansatte_vagter.find('Vagt', ['StartTid_Year', 'StartTid_Month', 'StartTid_Day', 'AnsatID'], [current_year, current_month, dag, id]) == False:
                    print('Tilføjer vagt for: ' + name + ' med start tidspunkt på: ' + s.start_entry.get() + ' og med slut tidspunkt på: ' + s.slut_entry.get())
                    ansatte_vagter.insert('Vagt',
                    ['StartTid_Year, StartTid_Month, StartTid_Day, StartTid_Hour, StartTid_Minute', 'SlutTid_Year, SlutTid_Month, SlutTid_Day, SlutTid_Hour, SlutTid_Minute', 'Uge_Dag', 'AnsatID'],
                    [current_year, current_month, dag, start_hour, start_minute, current_year, current_month, slut_dag, slut_hour, slut_minute, datetime.date(current_year, månede, dag).isocalendar()[1], id])
                    print([current_year, current_month, dag, start_hour, start_minute, current_year, current_month, slut_dag, slut_hour, slut_minute, datetime.date(current_year, månede, dag).isocalendar()[1], id])

                s.close()
            except:
                s.start_entry.delete(0, tk.END)
                s.slut_entry.delete(0, tk.END)
                s.dato_entry.delete(0, tk.END)
    def close(s):
        s.closed = True
        s.root.destroy()
class remove_product_window:
    def __init__(s, toplevel_size = [500, 400], window_name = 'Fjern vagt'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.closed = False
        s.root.protocol("WM_DELETE_WINDOW", s.close)

        #Ansattes navn
        s.name_label = tk.Label(s.root, text = "Navn", font = myFont)
        s.name_label.grid(row = 0, column = 0)

        s.dropdown_name_var = tk.StringVar(s.root)
        s.dropdown_name_options = []
        c = ansatte_vagter.con.cursor()
        c.execute('SELECT Navn FROM Ansatte')
        for x in c:
            s.dropdown_name_options.append(x[0])
        s.dropdown_name_var.set(s.dropdown_name_options[0]) # default value

        s.dropdown_name = tk.OptionMenu(s.root, s.dropdown_name_var, *s.dropdown_name_options)
        s.dropdown_name.config(font = myFont)
        s.dropdown_name.grid(row = 0, column = 1)

        #Tidsrummet
        s.dato_label = tk.Label(s.root, text = "Dato (dd.mm)", font = myFont)
        s.dato_label.grid(row = 1, column = 0)

        s.dato_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.dato_entry.grid(row = 1, column = 1)


        #buttons in bottom
        button_names = ['remove_shift', 'cancel']
        button_funcs = [s.remove_shift, s.close]
        button_texts = ['Fjern Vagt', 'Afbryd']
        s.buttons = {}
        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.root, text = button_texts[i], command = button_funcs[i], font = myFont).grid(row = 2, column = i), 'opened' : None}

    def remove_shift(s):
        dato = s.dato_entry.get().split('.')
        name = s.dropdown_name_var.get()

        if len(dato) != 2:
            s.dato_entry.delete(0, tk.END)
        else:
            try:
                dag = int(dato[0])
                månede = int(dato[1])

                ansat_id = ansatte_vagter.find('Ansatte', ['Navn'], [name], get = 'ID')
                vagt_id = ansatte_vagter.find('Vagt', ['AnsatID', 'StartTid_Month', 'StartTid_Day'], [ansat_id, månede, dag], get = 'ID')
                if vagt_id != False:
                    print('Fjerner en vagt for ' + name + ' den ' + str(dag) + "." + str(månede))
                    success = ansatte_vagter.remove('Vagt', vagt_id, edit_indexes = True)
                    if success:
                        print('havde success med at fjerne vagt fra ' + name)
                    else:
                        print(name + ' har ikke en vagt på den dato.')

                s.close()
            except:
                s.dato_entry.delete(0, tk.END)
    def close(s):
        s.closed = True
        s.root.destroy()


#roller (mangler edit_employees_role_window og remove_role_window)
class role_overall_window:
    def __init__(s, window_size = [500, 400], window_name = 'Roller'):
        s.root = tk.Toplevel(width = window_size[0], height = window_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.root.protocol("WM_DELETE_WINDOW", s.close)
        s.closed = False

        s.right_frame = tk.Frame(s.root, bg = 'red', width = window_size[0] * 0.5, height = window_size[1])
        s.left_frame = tk.Frame(s.root, bg = 'blue', width = window_size[0] * 0.5, height = window_size[1])

        s.left_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        s.right_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

        s.role_labels = []
        l = util.reverse([r.name.replace('_', ' ') for r in util.roller])
        for i in range(len(l)):
            s.role_labels.append(tk.Label(s.right_frame, text = str(i + 1) + '. ' + l[i] if login_window.rolle != (len(l) - i) else str(i + 1) + '. ' + l[i] + '(mig)', font = myFont))
            s.role_labels[-1].pack(side = tk.TOP, expand = True, fill = tk.X)

        if login_window.rolle >= util.roller.købmand.value:
            button_names = ['add_role', 'remove_role', 'edit_employees_role']
            button_funcs = [s.add_role, s.remove_role, s.edit_employees_role]
            button_texts = ['Tilføj Rolle', 'Fjern Rolle', 'Rediger Ansattes Rolle']
            s.buttons = {}
            for i in range(len(button_funcs)):
                s.buttons[button_names[i]] = {'button' : tk.Button(s.left_frame, text = button_texts[i], command = button_funcs[i], font = myFont).pack(fill = tk.X), 'opened' : None}

    def add_role(s):
        if s.buttons['add_role']['opened'] == None:
            s.buttons['add_role']['opened'] = add_role_window()
        elif s.buttons['add_role']['opened'].closed:
            s.buttons['add_role']['opened'] = add_role_window()
    def remove_role(s):
        if s.buttons['remove_role']['opened'] == None:
            s.buttons['remove_role']['opened'] = remove_role_window()
        elif s.buttons['remove_role']['opened'].closed:
            s.buttons['remove_role']['opened'] = remove_role_window()
    def edit_employees_role(s):
        if s.buttons['edit_employees_role']['opened'] == None:
            s.buttons['edit_employees_role']['opened'] = edit_employees_role_window()
        elif s.buttons['edit_employees_role']['opened'].closed:
            s.buttons['edit_employees_role']['opened'] = edit_employees_role_window()
    def close(s):
        s.closed = True
        s.root.destroy()
class add_role_window:

    def __init__(s, toplevel_size = [500, 400], window_name = 'Vagt oversigt'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.closed = False
        s.root.protocol("WM_DELETE_WINDOW", s.close)

        #UI Elements
        s.new_role_label = tk.Label(s.root, text = "Den nye rolle's navn", font = myFont)
        s.new_role_label.grid(row = 0, column = 0)

        s.new_role_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.new_role_entry.grid(row = 0, column = 1)

        s.all_roles = [r.name.replace('_', ' ') for r in util.roller]
        #s.all_roles.insert(0, '')
        #s.all_roles.append('')
        #dropdown lower
        s.role_lower_status_label = tk.Label(s.root, text = "Rolle under? (valgfri)", font = myFont)
        s.role_lower_status_label.grid(row = 1, column = 0)

        s.dropdown_lower_status_var = tk.StringVar(s.root)
        s.dropdown_lower_status_options = [s.all_roles[x] for x in range(len(s.all_roles))]
        s.dropdown_lower_status_var.set(s.all_roles[0]) # default value

        s.dropdown_lower_status = tk.OptionMenu(s.root, s.dropdown_lower_status_var, *s.dropdown_lower_status_options, command = s.lower_status_dropdown_change)
        s.dropdown_lower_status.config(font = myFont)
        s.dropdown_lower_status.grid(row = 1, column = 1)

        #dropdown upper
        s.role_upper_status_label = tk.Label(s.root, text = "Rolle over? (valgfri)", font = myFont)
        s.role_upper_status_label.grid(row = 2, column = 0)

        s.dropdown_upper_status_var = tk.StringVar(s.root)
        s.dropdown_upper_status_options = [s.all_roles[x] for x in range(len(s.all_roles))]
        s.dropdown_upper_status_var.set('') # default value

        s.dropdown_upper_status = tk.OptionMenu(s.root, s.dropdown_upper_status_var, *s.dropdown_upper_status_options, command = s.upper_status_dropdown_change)
        s.dropdown_upper_status.config(font = myFont)
        s.dropdown_upper_status.grid(row = 2, column = 1)

        #buttons in bottom
        button_names = ['add_role', 'cancel']
        button_funcs = [s.add_role, s.close]
        button_texts = ['Tilføj Rolle', 'Afbryd']
        s.buttons = {}
        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.root, text = button_texts[i], command = button_funcs[i], font = myFont).grid(row = 3, column = i), 'opened' : None}

    def lower_status_dropdown_change(s, event):
        s.dropdown_upper_status_var.set('')
        '''Virker ikke
        new_value = s.dropdown_lower_status_var.get()
        print(new_value)
        for x in s.all_roles:
            if x not in s.dropdown_lower_status_options and x != s.dropdown_upper_status_var.get():
                index = util.get_rolle_index(x.replace(' ', '_')) - 1
                print(index)
                if index > len(s.dropdown_lower_status_options):
                    index = len(s.dropdown_lower_status_options)

                s.dropdown_lower_status_options.insert(index, x)
                #s.dropdown_upper_status_options.insert(index, x)
                print(s.dropdown_lower_status_options)
                break
        s.dropdown_lower_status_var.set('')
        s.dropdown_lower_status['menu'].delete(0, 'end')
        for option in s.dropdown_lower_status_options:
            s.dropdown_lower_status['menu'].add_command(label = option, command = ex)
        #s.dropdown_lower_status.config(command = s.lower_status_dropdown_change)
        s.dropdown_lower_status_var.set(new_value)

        #s.dropdown_upper_status_options.remove(new_value)'''

    def upper_status_dropdown_change(s, event):
        s.dropdown_lower_status_var.set('')
        #print(s.dropdown_upper_status_var.get())

    def add_role(s):
        upper = s.dropdown_upper_status_var.get()
        if upper != '':
            upper = upper.replace(' ', '_')
            upper_index = util.get_rolle_index(upper)
        lower = s.dropdown_lower_status_var.get()
        if lower != '':
            lower = lower.replace(' ', '_')
            lower_index = util.get_rolle_index(lower)

        if upper != '':
            new_index = upper_index

            #først tilføj rollen til den lokale enum
            new_roles = [m.name for m in util.roller]
            new_roles.insert(new_index, s.new_role_entry.get())
            util.roller = enum.Enum('roller', new_roles)
            #for x in util.roller:
            #    print(str(x.name) + " : " + str(x.value))

            #til sidst ryk alle med den rolle
            done = False
            length = len(util.roller) - 1
            count = new_index + 1
            while done == False:
                ID = ansatte_vagter.find('Ansatte', ['Rolle'], [count], get = 'ID')
                if ID != False:
                    ansatte_vagter.edit('Ansatte', ID, 'Rolle', count + 1)
                elif count < length:
                    count += 1
                else:
                    done = True
            util.save_roller()
            s.close()
        elif lower != '':
            new_index = lower_index - 1

            #først tilføj rollen til den lokale enum
            new_roles = [m.name for m in util.roller]
            new_roles.insert(new_index, s.new_role_entry.get())
            util.roller = enum.Enum('roller', new_roles)
            #for x in util.roller:
            #    print(str(x.name) + " : " + str(x.value))

            #til sidst ryk alle med den rolle
            done = False
            length = len(util.roller) - 1
            count = new_index + 1
            while done == False:
                ID = ansatte_vagter.find('Ansatte', ['Rolle'], [count], get = 'ID')
                if ID != False:
                    ansatte_vagter.edit('Ansatte', ID, 'Rolle', count + 1)
                elif count < length:
                    count += 1
                else:
                    done = True
            util.save_roller()
            s.close()

    def close(s):
        s.closed = True
        s.root.destroy()
class edit_employees_role_window:
    def __init__(s, toplevel_size = [500, 400], window_name = 'Tilføj vagt'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.closed = False
        s.root.protocol("WM_DELETE_WINDOW", s.close)

        #Ansattes navn
        s.name_label = tk.Label(s.root, text = "Navn", font = myFont)
        s.name_label.grid(row = 0, column = 0)

        s.dropdown_name_var = tk.StringVar(s.root)
        s.dropdown_name_options = []
        c = ansatte_vagter.con.cursor()
        c.execute('SELECT Navn FROM Ansatte')
        for x in c:
            s.dropdown_name_options.append(x[0])
        s.dropdown_name_var.set(s.dropdown_name_options[0]) # default value

        s.dropdown_name = tk.OptionMenu(s.root, s.dropdown_name_var, *s.dropdown_name_options)
        s.dropdown_name.config(font = myFont)
        s.dropdown_name.grid(row = 0, column = 1)

        #Tidsrummet
        s.dato_label = tk.Label(s.root, text = "Dato (dd.mm)", font = myFont)
        s.dato_label.grid(row = 1, column = 0)

        s.dato_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.dato_entry.grid(row = 1, column = 1)

        s.start_label = tk.Label(s.root, text = "Start Tidspunkt (HH:MM)", font = myFont)
        s.start_label.grid(row = 2, column = 0)

        s.start_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.start_entry.grid(row = 2, column = 1)

        s.slut_label = tk.Label(s.root, text = "Slut Tidspunkt (HH:MM)", font = myFont)
        s.slut_label.grid(row = 3, column = 0)

        s.slut_entry = tk.Entry(s.root, font = myFont, justify = 'center', width = 8)
        s.slut_entry.grid(row = 3, column = 1)


        #buttons in bottom
        button_names = ['add_shift', 'cancel']
        button_funcs = [s.add_shift, s.close]
        button_texts = ['Tilføj Vagt', 'Afbryd']
        s.buttons = {}
        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.root, text = button_texts[i], command = button_funcs[i], font = myFont).grid(row = 4, column = i), 'opened' : None}

    def add_shift(s):
        start = s.start_entry.get().split(':')
        slut = s.slut_entry.get().split(':')
        dato = s.dato_entry.get().split('.')
        name = s.dropdown_name_var.get()

        if len(start) != 2 or len(slut) != 2 or len(dato) != 2:
            if len(start) != 2:
                s.start_entry.delete(0, tk.END)
            if len(slut) != 2:
                s.slut_entry.delete(0, tk.END)
            if len(dato) != 2:
                s.dato_entry.delete(0, tk.END)
        else:
            try:
                start_hour = int(start[0])
                start_minute = int(start[1])
                slut_hour = int(slut[0])
                slut_minute = int(slut[1])
                dag = int(dato[0])
                månede = int(dato[1])

                today = datetime.datetime.now().strftime("%Y/%m/%d/%H/%M/%S").split('/')
                current_year = int(today[0])
                current_month = int(today[1])
                current_day = int(today[2])
                current_hour = int(today[3])
                current_minute = int(today[4])
                current_second = int(today[5])
                week_number = datetime.date(current_year, current_month, current_day).isocalendar()[1]

                slut_dag = dag
                slut_månede = månede
                if current_month > månede:
                    current_year += 1 #jeg antager at man ikke kan få et vagt som foregår i to år på samme tid.
                if start_hour > slut_hour:
                    slut_dag += 1 #jeg antager at hvis man vælger f.eks. kl 22 som start_hour og 04 som slut_hour, så foregår vagten over to dage
                if start_hour > slut_hour or start_hour == slut_hour and start_minute > slut_minute:
                    start_hour, slut_hour = util.swap(start_hour, slut_hour)

                id = ansatte_vagter.find('Ansatte', ['Navn'], [name], get = 'ID')
                if ansatte_vagter.find('Vagt', ['StartTid_Year', 'StartTid_Month', 'StartTid_Day', 'AnsatID'], [current_year, current_month, dag, id]) == False:
                    print('Tilføjer vagt for: ' + name + ' med start tidspunkt på: ' + s.start_entry.get() + ' og med slut tidspunkt på: ' + s.slut_entry.get())
                    ansatte_vagter.insert('Vagt',
                    ['StartTid_Year, StartTid_Month, StartTid_Day, StartTid_Hour, StartTid_Minute', 'SlutTid_Year, SlutTid_Month, SlutTid_Day, SlutTid_Hour, SlutTid_Minute', 'Uge_Dag', 'AnsatID'],
                    [current_year, current_month, dag, start_hour, start_minute, current_year, current_month, slut_dag, slut_hour, slut_minute, datetime.date(current_year, månede, dag).isocalendar()[1], id])
                    print([current_year, current_month, dag, start_hour, start_minute, current_year, current_month, slut_dag, slut_hour, slut_minute, datetime.date(current_year, månede, dag).isocalendar()[1], id])

                s.close()
            except:
                s.start_entry.delete(0, tk.END)
                s.slut_entry.delete(0, tk.END)
                s.dato_entry.delete(0, tk.END)
    def close(s):
        s.closed = True
        s.root.destroy()
class remove_role_window:
    def __init__(s, window_size = [500, 400], window_name = 'Fjern Rolle'):
        s.root = tk.Toplevel(width = window_size[0], height = window_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.closed = False
        s.root.protocol("WM_DELETE_WINDOW", s.close)

        #UI Elements
        s.role_label = tk.Label(s.root, text = "Role", font = myFont)
        s.role_label.grid(row = 0, column = 0)

        s.dropdown_role_options = [r.name.replace('_', ' ') for r in util.roller]
        s.dropdown_role_var = tk.StringVar(s.root)
        s.dropdown_role_var.set(s.dropdown_role_options[0]) # default value

        s.dropdown_role = tk.OptionMenu(s.root, s.dropdown_role_var, *s.dropdown_role_options)
        s.dropdown_role.config(font = myFont)
        s.dropdown_role.grid(row = 0, column = 1)


        #buttons in bottom
        button_names = ['remove_role', 'cancel']
        button_funcs = [s.remove_role, s.close]
        button_texts = ['Fjern Rolle', 'Afbryd']
        s.buttons = {}
        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.root, text = button_texts[i], command = button_funcs[i], font = myFont).grid(row = 2, column = i), 'opened' : None}

    def remove_role(s):
        role = s.dropdown_role_var.get().replace(' ', '_')

        #først fjern rollen fra den lokale enum
        new_roles = []
        for m in util.roller:
            if m.name != role:
                new_roles.append(m.name)
        util.roller = enum.Enum('roller', new_roles)

        #derefter fjern den fra databasen
        util.rolle_data.find_and_remove('roller', ['rolle'], [role], edit_indexes = True)

        #til sidst ryk alle med den rolle der ønskes at fjernes en tak ned
        done = False
        role_value = util.get_rolle_index(role)
        while done == False:
            ID = ansatte_vagter.find('Ansatte', ['Rolle'], [role_value], get = 'ID')
            if ID != False:
                ansatte_vagter.edit('Ansatte', ID, 'Rolle', role_value - 1)
            else:
                done = True
        s.close()
    def close(s):
        s.closed = True
        s.root.destroy()

#profil
class profile_window:
    def __init__(s, toplevel_size = [500, 400], window_name = 'Roller'):
        s.root = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])
        if s.root != None:
            s.root.title(window_name)
        s.root.resizable(False, False)

        s.right_frame = tk.Frame(s, bg = 'red', width = window_size[0] * 0.5, height = window_size[1])
        s.left_frame = tk.Frame(s, bg = 'blue', width = window_size[0] * 0.5, height = window_size[1])

        s.left_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
        s.right_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

        s.role_labels = []
        l = list(util.roller)
        for i in l:
            s.role_labels.append(tk.Label(s, text = i, font = myFont))
            s.role_labels[-1].pack(side = tk.TOP)

        button_names = ['add_role', 'remove_role', 'edit_employees_role']
        button_funcs = [s.add_role, s.remove_role, s.edit_employees_role]
        button_texts = ['Tilføj Rolle', 'Fjern Rolle', 'Rediger Ansattes Rolle']
        s.buttons = {}
        for i in range(len(button_funcs)):
            s.buttons[button_names[i]] = {'button' : tk.Button(s.left_frame, text = button_texts[i], command = button_funcs[i], font = myFont).pack(fill = tk.X), 'opened' : None}

    def add_role(s):
        if s.buttons['add_role']['opened'] == None:
            s.buttons['add_role']['opened'] = add_role_window()
        elif s.buttons['add_role']['opened'].closed:
            s.buttons['add_role']['opened'] = add_role_window()
    def remove_role(s):
        if s.buttons['remove_role']['opened'] == None:
            s.buttons['remove_role']['opened'] = remove_role_window()
        elif s.buttons['remove_role']['opened'].closed:
            s.buttons['remove_role']['opened'] = remove_role_window()
    def edit_employees_role(s):
        if s.buttons['edit_employees_role']['opened'] == None:
            s.buttons['edit_employees_role']['opened'] = edit_employees_role_window()
        elif s.buttons['edit_employees_role']['opened'].closed:
            s.buttons['edit_employees_role']['opened'] = edit_employees_role_window()

#names = [m.name for m in util.roller] + ['newname1', 'newname2']
#util.roller = enum.Enum('roller', names)

#Det er her alle vinduerne bliver åbnet
#tester = yes_no_window([300, 200])
login_window = login_register_window()
if login_window.rolle > util.roller.kunde.value:
    #rolle = util.roller.butiks_chef.value #til testing
    main_window = ansat_window()
elif login_window.rolle == util.roller.kunde.value:
    main_window = kunde_window(window_name = login_window.navn + ' Hjem')
else:
    print('Du loggede ikke ind, så prøv igen senere')
    time.sleep(2)
