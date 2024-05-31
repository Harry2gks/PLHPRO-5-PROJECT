from MeetMePack.BackEnd.display import *
from MeetMePack.FrontEnd.PopUp_windows import pop_up
import tkinter as tk


# function No 1
def edit_client_rantevou(conn, new_window4, code_value, date_value, start_value, during_value):
    updated_appointment = change_appointment_details(conn, appointment_id=code_value.get(), new_date=date_value.get(), new_start_time=start_value.get(), new_duration=during_value.get())
    new_window4.destroy()
    if updated_appointment != 0:
        root = tk.Tk()
        root.withdraw()
        pop_up(root, notification="To ραντεβού ενημερώθηκε!")
        root.mainloop()
    else:
        root = tk.Tk()
        root.withdraw()
        pop_up(root, notification="Δεν υπάρχει διαθεσιμότητα!")
        root.mainloop()
