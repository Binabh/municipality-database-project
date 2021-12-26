import psycopg2

conn = psycopg2.connect(database = "municipality_db", user = "postgres", password = "postgres", host = "postgres_container", port = "5432")
print("Opened database successfully")
cur = conn.cursor()
def quit_or_continue():
    ask = input("[q]uit or [c]ontinue ? :")
    if(ask.lower() == "q"):
        cur.close()
        conn.close()
        return
    elif(ask.lower() == "c"):
        main()
    else:
        quit_or_continue()

def create_table():
    cur.execute(open("CreateTables.sql", "r").read())
    conn.commit()
    print("Tables created successfully!")
    quit_or_continue()

def delete_tables():
    cur.execute(open("DeleteTables.sql", "r").read())
    conn.commit()
    print("Tables deleted successfully!")
    quit_or_continue()

def insert_data():
    cur.execute(open("InsertData.sql", "r").read())
    conn.commit()
    print("Data inserted successfully!")
    quit_or_continue()

def query_data():
    # TODO: ADD SQL CODE
    print("Data queried successfully!")
    quit_or_continue()

def main():
    choice = input("What you want to do?\n1. Create tables\n2. Populate Tables\n3. Drop tables\n4. Query Data\n5. Exit\n")
    if(choice == "1"):
        create_table()
    elif(choice == "2"):
        insert_data()
    elif(choice == "3"):
        delete_tables()
    elif(choice == "4"):
        query_data()
    elif(choice == "5"):
        cur.close()
        conn.close()
        return
    else:
        print("Invalid choice! Please re-enter.")
        main()

main()
