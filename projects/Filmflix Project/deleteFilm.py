from dbConnectFilmflix import *
import readFilm
import time

def delete():
    # filmID to be deleted
    idField = input("Enter the filmID of the film to be deleted: ")
    # Method 1
    #              DELETE FROM tblFilms WHERE filmID=1, OR 2, OR 4...
    cursor.execute("DELETE FROM tblFilms WHERE filmID=" + idField)
    conn.commit()
    print(
        f"Record {idField} deleted from tblFilms Table"
    )  # display filmID deleted from the tblFilms table/database
    time.sleep(3)  # delay for 3 seconds then execute the code belo
    "filename.subroutineName()"
    readFilm.printData() # invoke the read subroutine for the read tblFilms file/app

#delete()