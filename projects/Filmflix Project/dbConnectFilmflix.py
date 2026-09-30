import sqlite3  # import the sqlite modele/package

"create a variable 'conn' and pass the sqlite connect method to it"

conn = sqlite3.connect("Filmflix Project/filmflix.db")  # pass folderpath/filename.db
# cursor method iterates through the database/tables
cursor = conn.cursor()
