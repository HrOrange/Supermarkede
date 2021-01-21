#tkinter imports
import tkinter as tk

#generic imports
import time
import random
import math
import utility as util #from another file
import database #from another file


ansatte_data = database.Data("Ansatte", columns = ['Navn STRING', 'Kodeord STRING', 'Løn REAL', 'Fyret INT', 'Rolle INT'], randoms = [['peter', 'hans', 4.5, 0, util.roller.butiks_chef.value], ['harry', 'klarry', 1200.2, 1, util.roller.butiks_chef.value], ['zahir', 'carl', -1, 0, util.roller.service_medarbejder.value]])
ansatte_data.print()

users_data = database.Data("Kunder", columns = ['Navn STRING', 'Kodeord STRING'], randoms = [['Joachim','1234'], ['Nicolai', '4321'], ['Michael', '1'], ['Alexander', '2'], ['Anders', '3']])
#users_data.print()

Vare_data = database.Data_Alternative(
names = ['VagtLink', 'Vagt'],
column_names = [['PersonID', 'VagtID'], ['StartTid_Year', 'StartTid_Month', 'StartTid_Day', 'StartTid_Hour', 'StartTid_Minute', 'SlutTid_Year', 'SlutTid_Month', 'SlutTid_day', 'SlutTid_Hour', 'SlutTid_Minute']],
column_types = [['INT', 'INT'], ['INT' for x in range(10)]],
randoms = [[], [[2020, 5, 24, 12, 30, 2020, 24, 5, 16, 30], [2020, 11, 10, 10, 30, 2021, 3, 25, 20, 30]]])

#vagter = database.Data("vagter")
#kunde_data = database.Data("vare")

#myFont = font.Font(family='Helvetica', size = 15, weight = "bold")
class login_register_window(tk.Frame):
    def __init__(s, master = None, window_size = [300, 200], window_name = 'Login/Registrer'):
        s.root = master
        tk.Frame.__init__(s, master)
        if master != None:
            master.title(window_name)

        #my_frame = tk.Frame(s, width = 300, height = 300)
        #my_frame.place(width=200, height=200)
        #s.root.protocol("WM_DELETE_WINDOW", lambda : s.root.destroy())

        s.place(width = window_size[0], height = window_size[1])
        #person information. Vi skulle måske lave en hel klasse til dette.
        s.ansat = False
        s.kunde = False
        s.navn = ''
        s.kodeord = ''
        s.rolle = 0

        #labels
        s.name_label = tk.Label(s, text = "Name", font = ('Helvetica', '15', 'bold'))
        s.name_label.place(relx = 0.17, rely = 0.25, width = window_size[0] * 0.6, height = window_size[1] * 0.15, anchor = tk.CENTER)
        s.password_label = tk.Label(s, text = "Password", font = ('Helvetica', '15', 'bold'))
        s.password_label.place(relx = 0.17, rely = 0.4, width = window_size[0] * 0.6, height = window_size[1] * 0.15, anchor = tk.CENTER)

        #entries
        s.name_entry = tk.Entry(s, font = ('Helvetica', '15', 'bold'))
        s.name_entry.place(relx = 0.65, rely = 0.25, width = window_size[0] * 0.6, height = window_size[1] * 0.15, anchor = tk.CENTER)
        s.password_entry = tk.Entry(s, font = ('Helvetica', '15', 'bold'))
        s.password_entry.place(relx = 0.65, rely = 0.4, width = window_size[0] * 0.6, height = window_size[1] * 0.15, anchor = tk.CENTER)

        #buttons
        button_size = [200, 50]
        s.login_button = tk.Button(s, text="Login", command = s.login, font = ('Helvetica', '15', 'bold'))
        s.login_button.place(relx = 0.5, rely = 0.65, width = window_size[0] * 0.8, height = window_size[1] * 0.2, anchor = tk.CENTER)
        s.registrer_button = tk.Button(s, text="Registrer", command = s.registrer, font = ('Helvetica', '15', 'bold'))
        s.registrer_button.place(relx = 0.5, rely = 0.85, width = window_size[0] * 0.8, height = window_size[1] * 0.2, anchor = tk.CENTER)
    def confirm_role(s):
        if s.name == '':
            name = s.name_entry.get()
            password = s.password_entry.get()

            #s.rolle = ansatte_data.get('')

    def login(s):
        name = s.name_entry.get()
        password = s.password_entry.get()

        s.ansat = ansatte_data.find(['Navn', 'Kodeord'], [name, password])
        if s.ansat == False:
            s.kunde = user_data.find(['Navn', 'Kodeord'], [name, password])

        if s.kunde or s.ansat:
            print("logged in")
            s.navn = name
            s.kodeord = password
            #s.rolle = ansatte_data.find(['Navn', 'Kodeord'], [name, password], get = 'Rolle')
            s.close()
        else:
            print('Navn eller kodeord er forkert')
    def registrer(s):
        name = s.name_entry.get()
        password = s.password_entry.get()

        findes_i_database = ansatte_data.find(['Navn', 'Kodeord'], [name, password])

        #s.role = "boss"

        if findes_i_database:
            s.name_entry.set('')
            s.password_entry.set('')
        else:
            print("registered")
            s.navn = name
            s.kodeord = password
            s.ansat = True
            #ansatte_data.insert(s.navn, s.kodeord)
            s.close()
    def close(s):
        s.root.destroy()

role = None
window_size = [300, 200]
root = tk.Tk()
root.geometry(str(window_size[0]) + "x" + str(window_size[1]))
login_window = login_register_window(root)
login_window.mainloop()

#print(login_window.role)

myFont = ('Helvetica', '15', "bold")
class shift_overview_window(tk.Toplevel):
    def __init__(s, toplevel_size):
        tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])

        s.cat = tk.Canvas(window, height = toplevel_size[0], width = toplevel_size[1], bg='white')
        s.cat.pack(fill = tk.BOTH, expand = True)

        offX = int(toplevel_size[0] / 7)
        for i in range(0, toplevel_size[0], offX):
            s.cat.create_line([(i, 0), (i, toplevel_size[1])])

        offY = int(toplevel_size[1] / 5)
        for i in range(0, toplevel_size[1], offY):
            s.cat.create_line([(0, i), (toplevel_size[0], i)])
class ansat_window(tk.Frame):
    def __init__(s, master = None, window_size = [600, 400], window_name = 'Ansat konsol'):
        s.root = master
        s.root.geometry(str(window_size[0]) + "x" + str(window_size[1]))
        tk.Frame.__init__(s, master)
        s.pack()
        #s.place(width = window_size[0], height = window_size[1])
        if master != None:
            master.title(window_name)
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
        if(rolle >= util.roller.butiks_chef.value):
            #toplevel_size = [400, 400]

            s.buttons = {}
            variable_names = ['give_role_button', 'edit_role_button', 'edit_price_button', 'shift_overview_button']
            texts = ['Giv Rolle', 'Rediger Rolle', 'Rediger Pris', 'Vagt Oversigt']
            funcs = [s.give_role, s.edit_role, s.edit_pris, s.shift_overview]
            for i in range(len(texts)):
                s.buttons[variable_names[i]] = tk.Button(s.left_frame, text = texts[i], command = funcs[i], font = myFont)
                #s.buttons[variable_names[i]].place(relx = 0.5, rely = (i + 0.5) / len(texts), relwidth = 1, relheight = 1 / len(texts), anchor = tk.CENTER)
                s.buttons[variable_names[i]].pack(expand = True, fill = tk.BOTH)

            #this is the same as above, just you know, more boring and hardcoded
            #s.give_role_button = tk.Button(left_frame, text = "Giv Rolle", command = give_role).pack(side = tk.TOP)
            #s.edit_role_button = tk.Button(left_frame, text = "Rediger Rolle", command = edit_role).pack(side = tk.TOP)
            #s.edit_price_button = tk.Button(left_frame, text = "Rediger Pris", command = edit_pris).pack(side = tk.TOP)
            #s.shift_overview_button = tk.Button(left_frame, text = "Vagt Oversigt", command = shift_overview).pack(side = tk.TOP)
    def edit_pris(s):
        #TODO: open toplevel
        pass
    def give_role(s):
        #TODO: make toplevel class to this specific, well problem. Might wanna combine this toplevel with the one needed for other role tasks
        pass
    def edit_role(s):
        #TODO: open toplevel
        pass
    def shift_overview(s):
        #TODO: open toplevel
        pass
    def window_resize_event(s, event):
        size = int(20 * (0.4 * s.root.winfo_width() / originial_window_size[0] + 0.6 * s.root.winfo_height() / originial_window_size[1]))
        for i in buttons:
            s.buttons[i]['font'] = s.myFont
    def close(s):
        s.root.destroy()
rolle = util.roller.butiks_chef.value
print(rolle)
root = tk.Tk()
main_window = ansat_window(root)
main_window.mainloop()
