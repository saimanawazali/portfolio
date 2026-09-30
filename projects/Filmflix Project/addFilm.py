from dbConnectFilmflix import *
import time

# create a subroutine to add record/data to the table tblFilms in filmflix.db database

def film():
    #create an empty list
    filmList = []

    title = input ("Enter film Title: ")
    year = input ("Enter year of release: ")
    rating = input ("Enter the film rating as PG/R: ")
    duration = input ("Enter the duration: ")
    genre = input ("Enter film genre: ")
    
# append captured data from user to the filmList = []
# tblFilms.filmID is autoincrement and would be added automatically
    filmList.append(title)
    filmList.append(year)
    filmList.append(rating)
    filmList.append(duration)
    filmList.append(genre)

#insert the dat from the list into the table tblFilms in
    cursor.execute("INSERT INTO tblFilms VALUES(NULL, ?,?,?,?,?)", filmList)
    conn.commit() # use commit method to write the changes to the database permanently
    print(f"{title} added to tblFilms Table")# display film name added to the table/database
    time.sleep(3) #delay for 3 seconds then execute the code below

# read data from the table tblFilms from filmflix.db database
    cursor.execute("SELECT * FROM tblFilms") # select all films
    row = cursor.fetchall() # fetch all data from the tblFilms table and pass it to the row variable
    for record in row: # iterate through the row (held data/values) variable
        print(record) # print every record in its own line

#film()  # call or invoke the subroutine