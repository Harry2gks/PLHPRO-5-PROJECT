import tkinter as tk
from tkinter import ttk
from MeetMePack.database import *
from MeetMePack.client import *
from MeetMePack.appointment import *
from MeetMePack.display import *

# function No1
def save_edit_rantevou_local(conn, code_value, date_value, start_value, during_value, end_value, new_window2):
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
        new_window2.destroy()
    else:
        pass  # Δεν υπάρχει ραντεβού