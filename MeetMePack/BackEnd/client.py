import sqlite3


def add_client(conn, name, surname, phone, email):
    """Add new client"""
    try:
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO clients (name, surname, phone, email)
            VALUES (?, ?, ?, ?)""", (name, surname, phone, email))
        conn.commit()
        print("O νέος πελάτης καταχωρήθηκε επιτυχώς")
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # undo all changes
        try:
            conn.rollback()
        except:
            print("Failed to undo all changes")
        return None


def change_client_details(conn, client_id, new_name=None, new_surname=None, new_phone=None, new_email=None):
    """Change client's details
        Choose which fields you want to change and the rest remain the same"""
    try:
        # Save in Dictionary the fields which change
        changes = {}
        if new_name is not None:
            changes['name'] = new_name
        if new_surname is not None:
            changes['surname'] = new_surname
        if new_phone is not None:
            changes['phone'] = new_phone
        if new_email is not None:
            changes['email'] = new_email

        # If there are no changes, end the function
        if not changes:
            print("No changes provided.")
            return

        # Create the query for execute, use dictionary keys and a loop for dynamically results
        set_fields = ', '.join([f"{key} = ?" for key in changes.keys()])
        set_criterion = f"UPDATE clients SET {set_fields} WHERE id = ?"

        cur = conn.cursor()
        cur.execute(set_criterion, list(changes.values()) + [client_id])
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # undo all changes
        try:
            conn.rollback()
        except:
            print("Failed to undo all changes")
        return None


def delete_client(conn, client_id):
    """Delete client"""
    try:

        # first delete the client's appointment
        client_appointment = appointments_per_client(conn, client_id=client_id)
        for appointment in client_appointment:
            delete_appointment(conn, appointment[0])

        # After delete the client
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM clients
            WHERE id = ?""", (client_id,))
        conn.commit()
        print("O  πελάτης διαγράφηκε επιτυχώς")
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # undo all changes
        try:
            conn.rollback()
        except:
            print("Failed to undo all changes")
        return None


def search_client_by_phone(conn, phone):
    """Search client by phone and return you their id or 0 if client doesn't exist"""
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM clients
            WHERE phone = ?""", (phone,))
        client = cur.fetchone()
        if client:
            return client
        else:
            return 0
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None


def search_client_by_email(conn, email):
    """Search client by phone and return you their id or 0 if client doesn't exist"""
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM clients
            WHERE email = ?""", (email,))
        client = cur.fetchone()
        if client:
            return client
        else:
            return 0
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None


def search_client_by_id(conn, id):
    """Search client by phone and return you their id or 0 if client doesn't exist"""
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM clients
            WHERE id = ?""", (id,))
        client = cur.fetchone()
        if client:
            return client
        else:
            return 0
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None
