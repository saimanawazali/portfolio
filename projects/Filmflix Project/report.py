from dbConnectFilmflix import *

def filmGenre():
    # filmID to be updated
    genreFilm = input("Enter the genre of the films to be printed \n(Comedy, Test, Action, Crime, Animation, Fantasy, Fighting): ")
    fieldValue = "'" + genreFilm +"'"
    cursor.execute(f"SELECT * FROM tblFilms where genre= {fieldValue}")  # select all data
    row = (cursor.fetchall())  # fetch all data from the tblFilms table and pass it to the row variable
    for record in row:  # iterate through the row (held data/values) variable
         print(record) 
    print(f"The film for genre {genreFilm}")

#filmGenre()

def filmYear():
    # filmID to be updated
    yearFilm = input("Enter the year for the films to be printed : ")
    fieldValue = "'" + yearFilm +"'"
    cursor.execute(f"SELECT * FROM tblFilms where yearReleased= {fieldValue}")  # select all data
    row = (cursor.fetchall())  # fetch all data from the tblFilms table and pass it to the row variable
    for record in row:  # iterate through the row (held data/values) variable
         print(record) 
    print(f"The film for year {yearFilm}")

#filmYear()

def filmRating():
    # filmID to be updated
    ratingFilm = input("Enter the rating for the films to be printed (PG/R):")
    fieldValue = "'" + ratingFilm +"'"
    cursor.execute(f"SELECT * FROM tblFilms where rating= {fieldValue}")  # select all data
    row = (cursor.fetchall())  # fetch all data from the tblFilms table and pass it to the row variable
    for record in row:  # iterate through the row (held data/values) variable
         print(record) 
    print(f"The film for rating {ratingFilm}")

#filmRating()