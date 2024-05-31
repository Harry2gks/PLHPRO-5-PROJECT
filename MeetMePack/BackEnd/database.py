import sqlite3
from MeetMePack.BackEnd.supporting_functions import resource_path


def connect_database():
    """Connection with database"""
    try:
        conn = sqlite3.connect('MeetMe_database.db')
        return conn
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # undo all changes
        try:
            conn.rollback()
        except:
            print("Failed to undo all changes")
        return None


def create_client(conn):
    """Create clients' table"""
    try:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS clients (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    surname TEXT NOT NULL,
                    phone INTEGER NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE
                    );""")
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # undo all changes
        try:
            conn.rollback()
        except:
            print("Failed to undo all changes")
        return None


def create_appointment(conn):
    """Create appointments' table"""
    try:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT NOT NULL,
                    duration INTEGER NOT NULL,
                    client_id INTEGER NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES clients(id)
                    );""")
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # undo all changes
        try:
            conn.rollback()
        except:
            print("Failed to undo all changes")
        return None


def run():
    conn = connect_database()
    create_client(conn)
    create_appointment(conn)
    return conn
