from MeetMePack.BackEnd.display import *
from MeetMePack.FrontEnd.PopUp_windows import pop_up
from MeetMePack.ConnectBackFrontEnd.tools import *
import tkinter as tk


search_by = "phone"     #global default search field
editable_fields = False  #global if fields are in editable mode or not
new_client_process = False #global if we create a new client

# Local use
def clear_fields(id_value, name_value, surname_value, anti_search_value):
    change_entry_state_custom(entry=id_value, state="normal")
    id_value.delete(0, tk.END)
    change_entry_state_custom(entry=id_value, state="readonly")
    change_entry_state_custom(entry=name_value, state="normal")
    name_value.delete(0, tk.END)
    change_entry_state_custom(entry=name_value, state="readonly")
    change_entry_state_custom(entry=surname_value, state="normal")
    surname_value.delete(0, tk.END)
    change_entry_state_custom(entry=surname_value, state="readonly")
    change_entry_state_custom(entry=anti_search_value, state="normal")
    anti_search_value.delete(0, tk.END)
    change_entry_state_custom(entry=anti_search_value, state="readonly")


# Function No 2
def phone_search_action(search_value, search_label, anti_search_label, id_value, name_value, surname_value, anti_search_value):
    global editable_fields
    global new_client_process
    editable_fields = False
    new_client_process = False
    change_entry_state_custom(entry=search_value, state="normal")
    search_value.delete(0, tk.END)
    clear_fields(id_value, name_value, surname_value, anti_search_value)
    global search_by
    search_by = "phone"
    search_label.configure(text="Τηλέφωνο")
    anti_search_label.configure(text="Email")


# Function No 3
def email_search_action(search_value, search_label, anti_search_label, id_value, name_value, surname_value, anti_search_value):
    global editable_fields
    global new_client_process
    editable_fields = False
    new_client_process = False
    change_entry_state_custom(entry=search_value, state="normal")
    search_value.delete(0, tk.END)
    clear_fields(id_value, name_value, surname_value, anti_search_value)
    global search_by
    search_by = "email"
    search_label.configure(text="Email")
    anti_search_label.configure(text="Τηλέφωνο")


# Function No 4
def add_client_local(id_value, search_value, name_value, surname_value, anti_search_value):
    global editable_fields
    editable_fields = False
    global new_client_process
    new_client_process = True
    change_entry_state_custom(entry=search_value, state="normal")
    search_value.delete(0, tk.END)
    change_entry_state_custom(entry=id_value, state="normal")
    id_value.delete(0, tk.END)
    change_entry_state_custom(entry=id_value, state="readonly")
    change_entry_state_custom(entry=surname_value, state="normal")
    search_value.delete(0, tk.END)
    change_entry_state_custom(entry=name_value, state="normal")
    name_value.delete(0, tk.END)
    change_entry_state_custom(entry=surname_value, state="normal")
    surname_value.delete(0, tk.END)
    change_entry_state_custom(entry=anti_search_value, state="normal")
    anti_search_value.delete(0, tk.END)


# Function No 5
def search_client_local(conn, search_value, id_value, name_value, surname_value, anti_search_value):
    global search_by
    clear_fields(id_value, name_value, surname_value, anti_search_value)
    if search_by == "phone":
        client = search_client_by_phone(conn, phone=search_value.get())
        if client == 0:
            root = tk.Tk()
            root.withdraw()
            pop_up(root, notification="Δεν υπάρχει Πελάτης με τα στοιχεία που δώσατε!")
            root.mainloop()
        else:
            change_entry_state_custom(entry=search_value, state="readonly")
            change_entry_state_custom(entry=id_value, state="normal")
            id_value.insert(index=0, string=f"{client[0]}")
            change_entry_state_custom(entry=id_value, state="readonly")
            change_entry_state_custom(entry=name_value, state="normal")
            name_value.insert(index=0, string=f"{client[1]}")
            change_entry_state_custom(entry=name_value, state="readonly")
            change_entry_state_custom(entry=surname_value, state="normal")
            surname_value.insert(index=0, string=f"{client[2]}")
            change_entry_state_custom(entry=surname_value, state="readonly")
            change_entry_state_custom(entry=anti_search_value, state="normal")
            anti_search_value.insert(index=0, string=f"{client[4]}")
            change_entry_state_custom(entry=anti_search_value, state="readonly")
    elif search_by == "email":
        clear_fields(id_value, name_value, surname_value, anti_search_value)
        client = search_client_by_email(conn, email=search_value.get())
        if client == 0:
            root = tk.Tk()
            root.withdraw()
            pop_up(root, notification="Δεν υπάρχει Πελάτης με τα στοιχεία που δώσατε!")
            root.mainloop()
        else:
            change_entry_state_custom(entry=search_value, state="readonly")
            change_entry_state_custom(entry=id_value, state="normal")
            id_value.insert(index=0, string=f"{client[0]}")
            change_entry_state_custom(entry=id_value, state="readonly")
            change_entry_state_custom(entry=name_value, state="normal")
            name_value.insert(index=0, string=f"{client[1]}")
            change_entry_state_custom(entry=name_value, state="readonly")
            change_entry_state_custom(entry=surname_value, state="normal")
            surname_value.insert(index=0, string=f"{client[2]}")
            change_entry_state_custom(entry=surname_value, state="readonly")
            change_entry_state_custom(entry=anti_search_value, state="normal")
            anti_search_value.insert(index=0, string=f"{client[3]}")
            change_entry_state_custom(entry=anti_search_value, state="readonly")


# Function No 6
def edit_client(id_value, search_value, name_value, surname_value, anti_search_value):
    global new_client_process
    new_client_process = False
    global editable_fields
    if id_value.get() != "":
        editable_fields = True
        change_entry_state_custom(entry=search_value, state="normal")
        change_entry_state_custom(entry=name_value, state="normal")
        change_entry_state_custom(entry=surname_value, state="normal")
        change_entry_state_custom(entry=anti_search_value, state="normal")


# Function No 7
def delete_client_local(conn, id_value, search_value, name_value, surname_value, anti_search_value):
    if id_value.get() != "":
        delete_client(conn, id_value.get())
        change_entry_state_custom(entry=search_value, state="normal")
        search_value.delete(0, tk.END)
        clear_fields(id_value, name_value, surname_value, anti_search_value)


# Function No 8
def save_changes(conn, id_value, name_value, surname_value, search_value, anti_search_value):
    global editable_fields
    global search_by
    global new_client_process
    if id_value.get() != "" and editable_fields:
        if search_by == "phone":
            change_client_details(conn, id_value.get(), new_name=name_value.get(), new_surname=surname_value.get(),
                                  new_phone=search_value.get(), new_email=anti_search_value.get())
        elif search_by == "email":
            change_client_details(conn, id_value.get(), new_name=name_value.get(), new_surname=surname_value.get(),
                                  new_phone=anti_search_value.get(), new_email=search_value.get())
        editable_fields = False
    elif new_client_process:
        if search_by == "phone":
            check1 = search_client_by_phone(conn, phone=search_value.get())
            check2 = search_client_by_email(conn, email=anti_search_value.get())
            if check1 == 0 and check2 == 0:
                add_client(conn, name=name_value.get(), surname=surname_value.get(), phone=search_value.get(),
                           email=anti_search_value.get())
                change_entry_state_custom(entry=id_value, state="normal")
                id_value.insert(0, f"{search_client_by_phone(conn, search_value.get())[0]}")
                change_entry_state_custom(entry=id_value, state="readonly")
                change_entry_state_custom(entry=search_value, state="readonly")
                change_entry_state_custom(entry=name_value, state="readonly")
                change_entry_state_custom(entry=surname_value, state="readonly")
                change_entry_state_custom(entry=anti_search_value, state="readonly")
                root = tk.Tk()
                root.withdraw()
                pop_up(root, notification="Ο πελάτης καταχωρήθηκε επιτυχώς!")
                root.mainloop()
            elif check1 != 0 or check2 != 0:
                print("Ο πελάτης είναι ήδη καταχωρημένος")
                root = tk.Tk()
                root.withdraw()
                pop_up(root, notification="Ο πελάτης είναι ήδη καταχωρημένος!")
                root.mainloop()
                check1 = None
                check2 = None
                return 0
        elif search_by == "email":
            check1 = search_client_by_phone(conn, phone=anti_search_value.get())
            check2 = search_client_by_email(conn, email=search_value.get())
            if check1 == 0 and check2 == 0:
                add_client(conn, name=name_value.get(), surname=surname_value.get(), phone=anti_search_value.get(),
                           email=search_value.get())
                change_entry_state_custom(entry=id_value, state="normal")
                id_value.insert(0, f"{search_client_by_phone(conn, anti_search_value.get())[0]}")
                change_entry_state_custom(entry=id_value, state="readonly")
                change_entry_state_custom(entry=search_value, state="readonly")
                change_entry_state_custom(entry=name_value, state="readonly")
                change_entry_state_custom(entry=surname_value, state="readonly")
                change_entry_state_custom(entry=anti_search_value, state="readonly")
                root = tk.Tk()
                root.withdraw()
                pop_up(root, notification="Ο πελάτης καταχωρήθηκε επιτυχώς!")
                root.mainloop()
            elif check1 != 0 or check2 != 0:
                print("Ο πελάτης είναι ήδη καταχωρημένος")
                root = tk.Tk()
                root.withdraw()
                pop_up(root, notification="Ο πελάτης είναι ήδη καταχωρημένος!")
                root.mainloop()
                check1 = None
                check2 = None
                return 0
        new_client_process = False
    change_entry_state_custom(entry=search_value, state="readonly")
    change_entry_state_custom(entry=name_value, state="readonly")
    change_entry_state_custom(entry=surname_value, state="readonly")
    change_entry_state_custom(entry=anti_search_value, state="readonly")


