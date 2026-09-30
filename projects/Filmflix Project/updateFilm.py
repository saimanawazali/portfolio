from dbConnectFilmflix import *
import readFilm
import time

def update():
    # filmID to be updated
    idField = input("Enter the FilmID of the film to be updated: ")
    # Enter the name of the field to be updated (title, releaseyear,rating,duration, genre)
    fieldName = input(
        "Which field would you like to update: (Title, YearReleased, Rating, Duration, Genre)? "
    ).title()
    # Enter the value of the fieldName to be updated
    fieldValue = input(f"Enter the new value for the {fieldName} field: ")
    print(f"The new value entered is {fieldValue}")

    # add single quotes around the new field value entered by the user
    fieldValue = "'" + fieldValue +"'"
    cursor.execute(f"UPDATE tblFilms SET {fieldName} = {fieldValue} WHERE filmID = {idField} ")
    conn.commit()
    print(f"Record {idField} Updated successfully!")
    time.sleep(3)
    readFilm.printData()

#update()