def change_entry_state_custom(entry, state):
    if state == "readonly":
        entry.configure(state="readonly", fg_color="#282c34")
    elif state == "normal":
        entry.configure(state="normal", fg_color="#343638")
