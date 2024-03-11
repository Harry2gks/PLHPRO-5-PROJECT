import tkinter as tk
from tkinter import ttk

# /////////////// ΠΕΛΑΤΟΛΟΓΙΟ /////////////////////////
def client_list():
    new_window = tk.Toplevel(root)
    new_window.title("Πελατολόγιο")
    new_window.geometry("500x500")  # Set width and height
    label = tk.Label(new_window, text="Πελατολόγιο")
    label.pack()

    enter_new_client_btn = tk.Button(new_window, text="Καταχώρηση Νέου Πελάτη", command=enter_new_client)
    enter_new_client_btn.pack(pady=5)
    
    search_client_btn = tk.Button(new_window, text="Προβολή Πελάτη", command=search_client)
    search_client_btn.pack(pady=5)

def enter_new_client():
    new_window = tk.Toplevel(root)
    new_window.title("Καρτέλα Πελάτη")
    new_window.geometry("500x500")  # Set width and height
    label = tk.Label(new_window, text="Καρτέλα Πελάτη")
    
    # Labels
    labels = ["id Πελατη", "Ονομα", "Επωνυμο", "Τηλεφωνο", "Email"]

    # Entry widgets
    entries = [tk.Entry(new_window) for _ in range(5)] # <--loop that creates single-line text input(tk.ENTRY). "_" exclude the loop variable from the body 

    #Display labels and entry widgets / placement on the grid
    for i in range(5):
        label = tk.Label(new_window, text=labels[i]) #anchor = "e" / aligns the label to the east of its grid cell / sticky throws an error
        entry = entries[i]
        label.grid(row=i, column=2, padx=10, pady=10, sticky='e')
        entry.grid(row=i, column=3, padx=10, pady=10, sticky='w')


    # Save and Discard/Delete buttons with icons
    #save_icon = tk.PhotoImage(file="path/to/save_icon.png")  # Replace with the actual path to your save icon <---- add icon
    #save_button = tk.Button(new_window, text="Save", image=save_icon, compound=tk.LEFT, command=save_appointment) <---- add icon
    save_button = ttk.Button(new_window, text="Save", compound=tk.LEFT)
    save_button.grid(row=11, column=1,  pady=10,  sticky='w')


   #discard_icon = tk.PhotoImage(file="path/to/discard_icon.png")  # Replace with the actual path to your discard icon <---- add icon
    #discard_button = tk.Button(new_window, text="Discard/Delete", image=discard_icon, compound=tk.LEFT, command=discard_appointment) <---- add icon
    discard_button = tk.Button(new_window, text="Discard/Delete", compound=tk.LEFT)
    discard_button.grid(row=11, column=3,  pady=10, padx=(0, 10), sticky='e')

    

def search_client():
    new_window = tk.Toplevel(root)
    new_window.title("καρτέλα Πελάτη")
    new_window.geometry("500x500")  # Set width and height
    label = tk.Label(new_window, text="καρτέλα Πελάτη")   

    # Labels
    labels = ["id Πελατη", "Ονομα", "Επωνυμο", "Τηλεφωνο", "Email"]

    # Entry widgets
    entries = [tk.Entry(new_window) for _ in range(5)] # <--loop that creates single-line text input(tk.ENTRY). "_" exclude the loop variable from the body 

    #Display labels and entry widgets / placement on the grid
    for i in range(1,3):
        label = tk.Label(new_window, text=labels[i], anchor='e') #anchor = "e" / aligns the label to the east of its grid cell / sticky throws an error
        entry = entries[i]
        label.grid(row=i, column=0, padx=10, pady=10, sticky='e')
        entry.grid(row=i, column=1, padx=10, pady=10, sticky='w') # sticky='w' / sticks the entry to the west side of its cell

    for i in range(3, 5):
        label = tk.Label(new_window, text=labels[i], anchor='e')
        entry = entries[i]
        label.grid(row=i-2, column=2, padx=10, pady=10, sticky='e')
        entry.grid(row=i-2, column=3, padx=10, pady=10, sticky='w')

        
    # <--- θέλει δουλεια η αναζήτηση! για κάθε ξεχωριστό input field χρειάζετε λούπα και έλεγχο --->
    search_button = tk.Button(new_window, width=2, height=1 ,command=lambda: search_appointments_by_client(search_var.get()))
    #search_icon = tk.PhotoImage(file="path/to/search_icon.png")  # Replace with the actual path to your search icon
    #search_button = ttk.Button(new_window, image=search_icon, command=lambda: search_appointments(search_var.get()))
    search_button.grid(row=2, column=4)
    
    label.pack()    

# /////////////// ΡΑΝΤΕΒΟΥ - ΛΙΣΤΑ /////////////////////////
def appointments():
    new_window = tk.Toplevel(root)
    new_window.title("Ραντεβού")
    new_window.geometry("500x500")  # Set width and height
    label = tk.Label(new_window, text="Ραντεβού")
    label.pack()

    new_appointment_btn = tk.Button(new_window, text="Νέο Ραντεβού", command=new_appointment)
    new_appointment_btn.pack(pady=5)
    
    show_apnt_by_day_btn = tk.Button(new_window, text="Προβολή Ραντεβού ανά ημέρα", command=show_apnt_by_day)
    show_apnt_by_day_btn.pack(pady=5)

    show_apnt_by_client_btn = tk.Button(new_window, text="Προβολή Ραντεβού ανά πελάτη", command=show_apnt_by_client)
    show_apnt_by_client_btn.pack(pady=5)

def new_appointment():
    new_window = tk.Toplevel(root)
    new_window.title("Καρτέλα Ραντεβού")
    new_window.geometry("500x500")  # Set width and height
    label = tk.Label(new_window, text="Καρτέλα Ραντεβού")
    
    # Labels
    labels = ["Κωδικος", "Ημερομηνια", "Απο", "Εως", "Διαρκεια", 
              "id Πελατη", "Ονομα", "Επωνυμο", "Τηλεφωνο", "Email"]

    # Entry widgets
    entries = [tk.Entry(new_window) for _ in range(10)] # <--loop that creates single-line text input(tk.ENTRY). "_" exclude the loop variable from the body 

    #Display labels and entry widgets / placement on the grid
    for i in range(5):
        label = tk.Label(new_window, text=labels[i], anchor='e') #anchor = "e" / aligns the label to the east of its grid cell / sticky throws an error
        entry = entries[i]
        label.grid(row=i, column=0, padx=10, pady=10, sticky='e')
        entry.grid(row=i, column=1, padx=10, pady=10, sticky='w') # sticky='w' / sticks the entry to the west side of its cell

    for i in range(5, 10):
        label = tk.Label(new_window, text=labels[i], anchor='e')
        entry = entries[i]
        label.grid(row=i-5, column=2, padx=10, pady=10, sticky='e')
        entry.grid(row=i-5, column=3, padx=10, pady=10, sticky='w')

    # Save and Discard/Delete buttons with icons
    #save_icon = tk.PhotoImage(file="path/to/save_icon.png")  # Replace with the actual path to your save icon <---- add icon
    #save_button = tk.Button(new_window, text="Save", image=save_icon, compound=tk.LEFT, command=save_appointment) <---- add icon
    save_button = ttk.Button(new_window, text="Save", compound=tk.LEFT)
    save_button.grid(row=10, column=0, columnspan=2, pady=10)

   # discard_icon = tk.PhotoImage(file="path/to/discard_icon.png")  # Replace with the actual path to your discard icon <---- add icon
    #discard_button = tk.Button(new_window, text="Discard/Delete", image=discard_icon, compound=tk.LEFT, command=discard_appointment) <---- add icon
    discard_button = tk.Button(new_window, text="Discard/Delete", compound=tk.LEFT, )
    discard_button.grid(row=10, column=2, columnspan=2, pady=10)
    
    label.pack()
    
def show_apnt_by_day():
    new_window = tk.Toplevel(root)
    new_window.title("Προβολή Ραντεβού ανά ημέρα")
    new_window.geometry("500x500")  # Set width and height

    # Search field and search button with icon
    search_var = tk.StringVar()
    search_entry = tk.Entry(new_window, textvariable=search_var, width=30)
    search_entry.grid(row=0, column=0, padx=10, pady=10)

    #search_icon = tk.PhotoImage(file="path/to/search_icon.png")  # Replace with the actual path to your search icon
    #search_button = ttk.Button(new_window, image=search_icon, command=lambda: search_appointments(search_var.get()))
    search_button = ttk.Button(new_window, command=lambda: search_appointments_by_day(search_var.get()))
    search_button.grid(row=0, column=1, padx=5, pady=10)

    # Add appointment display logic here ???

# Search function that displays results upon call on lamda function above
def search_appointments_by_day(query):        # <----------------- implement search 
    # Add search logic here
    print(f"Searching for appointments with query: {query}")

def show_apnt_by_client():
    new_window = tk.Toplevel(root)
    new_window.title("Προβολή Ραντεβού ανά πελάτη")
    new_window.geometry("500x500")  # Set width and height
    label = tk.Label(new_window, text="Προβολή Ραντεβού ανά πελάτη")   

    # Labels
    labels = ["id Πελατη", "Ονομα", "Επωνυμο", "Τηλεφωνο", "Email"]

    # Entry widgets
    entries = [tk.Entry(new_window) for _ in range(5)] # <--loop that creates single-line text input(tk.ENTRY). "_" exclude the loop variable from the body 

    #Display labels and entry widgets / placement on the grid
    for i in range(3):
        label = tk.Label(new_window, text=labels[i], anchor='e') #anchor = "e" / aligns the label to the east of its grid cell / sticky throws an error
        entry = entries[i]
        label.grid(row=i, column=0, padx=10, pady=10, sticky='e')
        entry.grid(row=i, column=1, padx=10, pady=10, sticky='w') # sticky='w' / sticks the entry to the west side of its cell

    for i in range(3, 5):
        label = tk.Label(new_window, text=labels[i], anchor='e')
        entry = entries[i]
        label.grid(row=i-2, column=2, padx=10, pady=10, sticky='e')
        entry.grid(row=i-2, column=3, padx=10, pady=10, sticky='w')

        
    # <--- θέλει δουλεια η αναζήτηση! για κάθε ξεχωριστό input field χρειάζετε λούπα και έλεγχο --->
    search_button = tk.Button(new_window, width=2, height=1 ,command=lambda: search_appointments_by_client(search_var.get()))
    #search_icon = tk.PhotoImage(file="path/to/search_icon.png")  # Replace with the actual path to your search icon
    #search_button = ttk.Button(new_window, image=search_icon, command=lambda: search_appointments(search_var.get()))
    search_button.grid(row=2, column=4)
    
    label.pack()    

# Search function that displays results upon call on lamda function above
def search_appointments_by_client(query):        # <----------------- implement search 
    # Add search logic here
    print(f"Searching for appointments with query: {query}")


# //////////////// Main window //////////////////
root = tk.Tk()
root.title("Main Window")
root.geometry("500x500")  # Set width and height

# Buttons
button1 = tk.Button(root, text="Πελατολόγιο", command=client_list)
button1.pack(pady=10)

button2 = tk.Button(root, text="Ραντεβού", command=appointments)
button2.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
