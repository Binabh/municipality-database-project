import psycopg2

conn = psycopg2.connect(database = "municipality_db", user = "postgres", password = "postgres", host = "postgres_container", port = "5432")
print("Opened database successfully")
cur = conn.cursor()

def create_table():
    # TODO: ADD SQL CODE
    print("Tables created successfully!")

def insert_data():
    # TODO: ADD SQL CODE
    print("Data inserted successfully!")

def query_data():
    # TODO: ADD SQL CODE
    print("Data queried successfully!")