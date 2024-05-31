import tkinter as tk
from MeetMePack.BackEnd.display import *
from MeetMePack.FrontEnd.PopUp_windows import pop_up

# function No1
def save_edit_rantevou_local(conn, code_value, date_value, start_value, during_value, end_value, new_window2, new_window3):
    new_rantevou = change_appointment_details(conn, appointment_id=code_value.get(),
                                              new_date=date_value.get(), new_start_time=start_value.get(),
                                              new_duration=during_value.get())
    if new_rantevou != 0:
        rantevou = search_appointment_by_id(conn, appointment_id=code_value.get())
        date_value.configure(state='readonly')
        start_value.configure(state='readonly')
        during_value.configure(state='readonly')
        end_value.configure(state='normal')
        end_value.delete(0, tk.END)
        end_value.insert(0, f"{rantevou[3]}")
        end_value.configure(state='readonly')
        new_window3.destroy()
        new_window2.destroy()
        root = tk.Tk()
        root.withdraw()
        pop_up(root, notification="To ραντεβού ενημερώθηκε!")
        root.mainloop()
    else:
        root = tk.Tk()
        root.withdraw()
        pop_up(root, notification="Δεν υπάρχει διαθεσιμότητα!")
        root.mainloop()