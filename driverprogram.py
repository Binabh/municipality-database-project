import psycopg2

conn = psycopg2.connect(database = "municipality_db", user = "postgres", password = "postgres", host = "postgres_container", port = "5432")
print("Opened database successfully")
cur = conn.cursor()

def create_table():
    cur.execute(open("CreateTables.sql", "r").read())
    print("Tables created successfully!")

def delete_table():
    cur.execute(open("DeleteTables.sql", "r").read())
    print("Tables deleted successfully!")

def insert_data():
    # TODO: ADD SQL CODE
    print("Data inserted successfully!")

def query_data():
    # TODO: ADD SQL CODE
    print("Data queried successfully!")

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
        return
    else:
        print("Invalid choice! Please re-enter.")
        main()

main()
