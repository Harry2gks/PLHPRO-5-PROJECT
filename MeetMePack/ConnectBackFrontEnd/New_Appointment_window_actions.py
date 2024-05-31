from MeetMePack.FrontEnd.clientAppointments_window import *


# function No1
def save_rantevou(conn, new_window3, code_value, id_client_value, date_value, start_value, during_value, end_value):
    if code_value.get() == "":
        id = add_appointment(conn, client_id=id_client_value.get(), date=date_value.get(),
                             start_time=start_value.get(), duration=during_value.get())
        if id != 0:
            rantevou = search_appointment_by_id(conn, appointment_id=id)
            code_value.configure(state='normal')
            code_value.insert(0, f"{rantevou[0]}")
            code_value.configure(state='readonly')
            end_value.configure(state='normal')
            end_value.insert(0, f"{rantevou[3]}")
            end_value.configure(state='readonly')
            date_value.configure(state='readonly')
            start_value.configure(state='readonly')
            during_value.configure(state='readonly')
            new_window3.destroy()
            root = tk.Tk()
            root.withdraw()
            pop_up(root, notification="Το ραντεβού αποθηκεύτηκε με επιτυχία!")
            root.mainloop()
        else:
            root = tk.Tk()
            root.withdraw()
            pop_up(root, notification="Δεν υπάρχει διαθεσιμότητα!")
            root.mainloop()

# function No2
def delete_appointment_local(conn, code_value, date_value, start_value, end_value, during_value):
    if code_value.get() != "":
        rantevou = search_appointment_by_id(conn, appointment_id=code_value.get())
        delete_appointment(conn, appointment_id=rantevou[0])
        code_value.configure(state='normal')
        code_value.delete(0, tk.END)
        code_value.configure(state='readonly')
        date_value.configure(state='normal')
        date_value.delete(0, tk.END)
        start_value.configure(state='normal')
        start_value.delete(0, tk.END)
        end_value.configure(state='normal')
        end_value.delete(0, tk.END)
        end_value.configure(state='readonly')
        during_value.configure(state='normal')
        during_value.delete(0, tk.END)
        during_value.insert(0, string="30")
        root = tk.Tk()
        root.withdraw()
        pop_up(root, notification="Το ραντεβού διαγράφτηκε!")
        root.mainloop()

