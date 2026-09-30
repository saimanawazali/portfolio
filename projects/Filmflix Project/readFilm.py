from dbConnectFilmflix import *

def printData():
     # read data from the table tblFilms in filmflix.db database
     cursor.execute("SELECT * FROM tblFilms")  # select all data
     row = (cursor.fetchall())  # fetch all data from the tblFilms table and pass it to the row variable
     for record in row:  # iterate through the row (held data/values) variable
         print(record)  # print every record in its own line
#printData()