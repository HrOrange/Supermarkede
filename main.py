#tkinter imports
import tkinter as tk
#import tkinter.font as font

#generic imports
import time
import random
import utility #from another file
import database #from another file

#vare_data = Data("vare")


ansatte_data = database.Data("ansatte", table_columns = ['navn STRING', 'løn REAL', 'fyret INT'], randoms = [['peter', 4.5, 0], ['harry', 1200.2, 1], ['zahir', -1, 0]])
ansatte_data.print()

users_data = database.Data("users", table_columns = ['navn STRING', 'password STRING'], randoms = [['Joachim','1234'], ['Nicolai', '4321'], ['Michael', '1'], ['Alexander', '2'], ['Anders', '3']])
users_data.print()

#vagter = database.Data("vagter")
#kunde_data = database.Data("vare")

#myFont = font.Font(family='Helvetica', size = 15, weight = "bold")
class login_register_window(tk.Frame):
    def __init__(s, master = None, window_size = [300, 200]):
        tk.Frame.__init__(s, master)

        #my_frame = tk.Frame(s, width = 300, height = 300)
        #my_frame.place(width=200, height=200)
        #s.root.protocol("WM_DELETE_WINDOW", lambda : s.root.destroy())

        s.place(width = window_size[0], height = window_size[1])
        s.got_in = False

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

    def login(s):
        name = s.name_entry.get()
        password = s.password_entry.get()

        s.got_in = users_data.check_user(name, password)

        if s.got_in:
            s.close()
        else:
            print('Nope')
    def registrer(s):
        name = s.name_entry.get()
        password = s.password_entry.get()

        role = "boss"
        s.got_in = users_data.check_user(name, password)

        if s.got_in:
            name_entry.set('')
            password_entry.set('')
        else:
            s.close()
    def close(s):
        s.destroy()

role = None
window_size = [300, 200]
root = tk.Tk()
root.geometry(str(window_size[0]) + "x" + str(window_size[1]))
root.title("Login/Registrer")
login_window = login_register_window(root)
login_window.mainloop()

print(login_window.got_in)

"""if login_window.check:
    #Her åbner vi main programmet
    window_size = [600, 400]
    originial_window_size = [window_size[0], window_size[1]]
    s.root = tk.Tk()
    s.root.geometry(str(window_size[0]) + "x" + str(window_size[1]))
    s.root.title("Supermarket")
    s.myFont = font.Font(family='Helvetica', size = 15, weight = "bold")

    def window_resize_event(event):
        s.myFont = font.Font(family='Helvetica', size = int(20 * (0.4 * s.root.winfo_width() / originial_window_size[0] + 0.6 * s.root.winfo_height() / originial_window_size[1])), weight = "bold")
        for i in buttons:
            buttons[i]['font'] = s.myFont
    s.root.bind('<Configure>', window_resize_event) #this calls the function window_resize_event whenever a window resize event is happening

    #frames
    right_frame = tk.Frame(s.root, bg = 'red', width = window_size[0] * 0.6, height = window_size[1])
    top_right_frame = tk.Frame(right_frame, bg = 'pink', width = window_size[0] * 0.6, height = window_size[1] * 0.6)
    bottom_right_frame = tk.Frame(right_frame, bg = 'orange', width = window_size[0] * 0.6, height = window_size[1] * 0.4)
    left_frame = tk.Frame(s.root, bg = 'blue', width = window_size[0] * 0.4, height = window_size[1])

    left_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    right_frame.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)
    bottom_right_frame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)
    top_right_frame.pack(side = tk.TOP, expand = True, fill = tk.BOTH)

    #buttons
    if(user_role == 'boss'):
        toplevel_size = [400, 400]
        def give_role():
            #TODO: open toplevel
            pass

        def edit_role():
            #TODO: open toplevel
            pass

        def edit_pris():
            #TODO: open toplevel
            pass

        def shift_overview():
            def add_shift():
                #TODO: open toplevel
                pass

            def edit_shift():
                #TODO: open toplevel
                pass

            def remove_shift():
                #TODO: open toplevel
                pass

            window = tk.Toplevel(width = toplevel_size[0], height = toplevel_size[1])

            cat = tk.Canvas(window, height = toplevel_size[0], width = toplevel_size[1], bg='white')
            cat.pack(fill = tk.BOTH, expand = True)

            offX = int(toplevel_size[0] / 7)
            for i in range(0, toplevel_size[0], offX):
                cat.create_line([(i, 0), (i, toplevel_size[1])])

            offY = int(toplevel_size[1] / 5)
            for i in range(0, toplevel_size[1], offY):
                cat.create_line([(0, i), (toplevel_size[0], i)])

            #add_shift_button = tk.Button(window, text = "Giv Vagt", command = add_shift).pack(side = tk.TOP)
            #edit_shift_button = tk.Button(window, text = "Rediger Vagt", command = add_shift).pack(side = tk.TOP)
            #remove_shift_button = tk.Button(window, text = "Fjern Vagt", command = remove_shift).pack(side = tk.TOP)

            window.mainloop()

        buttons = {}
        variable_names = ['give_role_button', 'edit_role_button', 'edit_price_button', 'shift_overview_button']
        texts = ['Giv Rolle', 'Rediger Rolle', 'Rediger Pris', 'Vagt Oversigt']
        funcs = [give_role, edit_role, edit_pris, shift_overview]
        for i in range(len(texts)):
            buttons[variable_names[i]] = tk.Button(left_frame, text = texts[i], command = funcs[i], font = s.myFont)
            buttons[variable_names[i]].place(relx = 0.5, rely = (i + 0.5) / len(texts), relwidth = 1, relheight = 1 / len(texts), anchor = tk.CENTER)

        #give_role_button = tk.Button(left_frame, text = "Giv Rolle", command = give_role).pack(side = tk.TOP)
        #edit_role_button = tk.Button(left_frame, text = "Rediger Rolle", command = edit_role).pack(side = tk.TOP)
        #edit_price_button = tk.Button(left_frame, text = "Rediger Pris", command = edit_pris).pack(side = tk.TOP)
        #shift_overview_button = tk.Button(left_frame, text = "Vagt Oversigt", command = shift_overview).pack(side = tk.TOP)

    s.root.mainloop()"""
    #objekter i programmet
