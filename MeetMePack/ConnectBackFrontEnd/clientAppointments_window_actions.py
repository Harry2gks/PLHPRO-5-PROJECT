from MeetMePack.BackEnd.display import *
import tkinter as tk
from MeetMePack.FrontEnd.PopUp_windows import pop_up


# function No 1
def del_appointment(conn, root, new_window2, id_value, name_value, surname_value, appointment):
    delete_appointment(conn, appointment_id=appointment[0])
    new_window2.destroy()
    root = tk.Tk()
    root.withdraw()
    pop_up(root, notification="Το ραντεβού διαγράφτηκε!")
    root.mainloop()


