import sqlite3, csv
from pathlib import Path

schema = Path("static\schema.sql")

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")
conn.executescript(schema.read_text()) # Creates table from file
conn.close()



#  path = "Data/"

# def getRowCounts(table, isReport=False):
#     cursor.execute(f"SELECT COUNT(*) FROM {table}")
#     result = cursor.fetchone()
#     row_count = result[0]
#     if isReport:
#         return(table, row_count)
#     return(row_count)


# # way of inserting data into the tables 
# # Ai used to fix binding error
# def insertData(csvFile, query, table,cols = 4, missFirstCol = True):
    
#     # Ensure that we don't insert the same csv multiple times
#     if getRowCounts(table) == 0:
#         if missFirstCol == True:
#             colMiss = 1
#         else:
#             colMiss = 0
       
#         with open(f"{path}{csvFile}", newline="") as file:
#             reader = csv.reader(file)
#             next(reader)
#             for row in reader:
                
#                 # filling empty values and miss the id column
#                 cleaned_row = [None if val == '' else val for val in row[colMiss:]]
                
#                 while len(cleaned_row) < cols:
#                     cleaned_row.append("NA")
#                 try:
#                     cursor.execute(query, cleaned_row)
                    
#                 except sqlite3.IntegrityError as e:
#                     print(f"Skipping row {row}: {e}")
                
#                 except sqlite3.ProgrammingError as e:
#                     print(f"Binding error in row {row}: {e}")
        
#         conn.commit()

# insertData(
#     'users.csv',
#     "INSERT INTO users (gender, age, region, join_date) VALUES (?, ?, ?, ?)",
#     "users"
# )
# insertData(
#     'activities.csv',
#     "INSERT INTO activities (user_id, date, activity_type, duration) VALUES (?, ?, ?, ?)",
#     "activities"
# )
# insertData(
#     'checkins.csv',
#     "INSERT INTO checkins (user_id, date, mood_score, sleep_hours) VALUES (?, ?, ?, ?)",
#     "checkins"
# )
# insertData(
#     'sessions.csv',
#     "INSERT INTO sessions (user_id, start_ts, end_ts, screen_time) VALUES (?, ?, ?, ?)",
#     "sessions"
# )
# insertData(
#     'subscriptions.csv',
#     "INSERT INTO subscriptions (user_id, plan, start_date, end_date) VALUES (?, ?, ?, ?)",
#     "subscriptions",
#     missFirstCol=False
# )


# tables = [
#     "users",
#     "activities",
#     "checkins",
#     "sessions",
#     "subscriptions"
# ]


# print("Table name, Row count")
# for table in tables:
#     print(getRowCounts(table, True))

# def getDates(table, column):
#     print(table)
#     print("MAX")
#     print(conn.execute(f"SELECT MAX({column}) FROM {table}").fetchone()[0])
#     print("MIN")
#     print(conn.execute(f"SELECT MIN({column}) FROM {table}").fetchone()[0])

# getDates(tables[1], "date")
# getDates(tables[2], "date")
# getDates(tables[3], "start_ts")
# getDates(tables[3], "end_ts")


