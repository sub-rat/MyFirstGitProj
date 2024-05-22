import sqlite3

sqliteConnection = sqlite3.connect('first_example.db')
print("Database connected")

cursor = sqliteConnection.cursor()
print("Database initialized")

create_table_query = """
CREATE TABLE IF NOT EXISTS emp  (id integer primary key AUTOINCREMENT, name text);
"""
cursor.execute(create_table_query)

insert_table_query = """
INSERT INTO emp(name) VALUES("arjun")
"""
cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name) VALUES("arjun")
"""
cursor.execute(insert_table_query)
insert_table_query = """
INSERT INTO emp(name) VALUES("arjun")
"""
cursor.execute(insert_table_query)
sqliteConnection.commit()

sqliteConnection.close()
