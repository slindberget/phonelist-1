#import sqlite3
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="phone2",
    user="phone2",
    password="abc123"
    )
def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Hello and welcome to the phone list, available commands: \nadd - add a phone number\ndelete - delete a contact \nlist - list all phone numbers \nquit - quit the program \nCommand: ").upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        add_phone(conn, name, phone)
    elif cmd == "DELETE":
        name = input("  Name: ")
        delete_phone(conn, name)
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    elif cmd != "LIST" or cmd != "ADD" or cmd != "DELETE" or cmd != "QUIT":
        print(f"Unknown command: {cmd}")
