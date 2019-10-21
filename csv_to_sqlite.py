import sqlite3
import csv

# create connection object for db
conn = sqlite3.connect('fungi_db')

# create cursor to execute SQL commands
c = conn.cursor()

# ------------------------------------------
# ------------------------------------------

# create SQL table
# 3 sets of quotes  = dot string, allows strings that span multiple lines
# c.execute("""CREATE TABLE findings(
#             id INTEGER,
#             date TEXT,
#             type TEXT,
#             finder TEXT,
#             notes TEXT,
#             lat REAL,
#             lon REAL,
#             nasref TEXT
#             )""")

# c.execute("DROP TABLE findings")

# ------------------------------------------
# ------------------------------------------

# load CSV data into table
# with open ('findings.csv', 'r') as f:
#     reader = csv.reader(f)
#     data = next(reader) 
#     query = 'INSERT INTO findings VALUES ({0})'
#     query = query.format(','.join('?' * len(data)))
#     for data in reader:
#         c.execute(query, data)

# ------------------------------------------
# ------------------------------------------

c.execute("SELECT * FROM findings")

# test / determine rows to dislplay
# print(c.fetchone())
# print(c.fetchmany(2))
print(c.fetchall())

# commit current transaction to db and close
conn.commit()
conn.close()





############################################
############################################
# Trial Stuff ##############################

# Winner! (read in csv to table): https://stackoverflow.com/questions/21257899/writing-a-csv-file-into-sql-server-database-using-python


# c.execute("CREATE TABLE findings (id STR, date STR, notes STR, lat STR, lon STR)")

# with open ('test.csv', 'r') as fin:
#     dr = csv.DictReader(fin)
#     to_db = [(i['id'], i['date'], i['notes'], i['lat'], i['lon']) for i in dr]

# c.executemany("INSERT INTO findings VALUES (?, ?, ?, ?, ?);", to_db)



# c.execute("INSERT INTO findings VALUES (10001, '10/12/19', 'found here', '45.9367', '-122.659')")