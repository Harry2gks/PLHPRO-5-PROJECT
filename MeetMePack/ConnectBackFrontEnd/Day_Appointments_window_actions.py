from MeetMePack.BackEnd.display import *
from MeetMePack.FrontEnd.PopUp_windows import *


# function No 1
def del_appointment_local_appointment(conn, new_window2, appointment):
    delete_appointment(conn, appointment_id=appointment[0])
    new_window2.destroy()
    root = tk.Tk()
    root.withdraw()
    pop_up(root, notification="Το ραντεβού διαγράφτηκε!")
    root.mainloop()


# function No 2
def export_xls_local(conn, search_entry):
    xls = extract_xls(conn, date=search_entry.get())
    if xls != 0:
        root = tk.Tk()
        root.withdraw()
        pop_up(root, notification="To αρχείο κατέβηκε επιτυχώς στο φάκελο Download!")
        root.mainloop()
    else:
        root = tk.Tk()
        root.withdraw()
        pop_up(root, notification="Υπήρξε κάποιο σφάλμα στην δημιουργία του αρχείου!")
        root.mainloop()


# function No 3
def email_local(conn, search_entry):
    emails = remind_email(conn, date=search_entry.get())
    if emails == 1:
        root = tk.Tk()
        root.withdraw()
        pop_up(root, notification="Τα emails στάλθηκαν με επιτυχία!")
        root.mainloop()
    else:
        root = tk.Tk()
        root.withdraw()
        pop_up(root, notification="Υπήρξε κάποιο σφάλμα στην αποστολή των emails!")
        root.mainloop()
