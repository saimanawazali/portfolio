import readFilm
import addFilm
import updateFilm
import deleteFilm
import report

# craate a function
def menuOptions():
    options = 0  # create a flag variable and initialise it with the value zero

    # check the value held in the options variable if it is in the list
    while options not in ["1", "2", "3", "4", "5"]:
        print(
            "FilmFlix Menu Options:\nEnter \n1. Print All Records. \n2. Add A Record. \n3. Amend A Record. \n4. Delete A Record. \n5. Exit"
        )
        #re-assign the options variable to an input function

        options = input("\nEnter one of the options above: ") # user enter 1 or 2 or 3 or 4 or 5
        # check/compare  user input with the items in the list
        if options not in ["1", "2", "3", "4", "5"]:
            print(f"{options} is not a valid choice!")
    return options

def reportOptions():
    options1 = 0  # create a flag variable and initialise it with the value zero

    # check the value held in the options variable if it is in the list
    while options1 not in ["1", "2", "3", "4", "5"]:
        print(
            "FilmFlix Reports Options:\nEnter \n1. Print All Films. \n2. Select a Genre. \n3. Select a Year. \n4. Select the Rating. \n5. Exit"
        )
        #re-assign the options variable to an input function

        options1 = input("\nEnter one of the options above: ") # user enter 1 or 2 or 3 or 4 or 5
        # check/compare  user input with the items in the list
        if options1 not in ["1", "2", "3", "4", "5"]:
            print(f"{options1} is not a valid choice!")
    return options1

    
#menuOptions()


# create a boolean flag variable and set it to True

mainProgram  = True  # assign mainProgram a boolean data type

# name = "jane"
#While name == "jane" .. do this and thi and thi...
opt=0

while opt not in ["1","2"]:
    print("FilmFlix Main Menu:")
    print("1.To Update FilmFlix Data\n2.To View Reports")
    print("3.Exit")
    opt = input("\nEnter one of the options above: ")

    if opt == "1":
        while mainProgram == True: #check/compare that main program equals to true
            mainMenu = menuOptions() # we passed in the menuOptions() function to the variable mainmenu
            # if options (1/2/3/4/5)
            # invoke or call the filename.subroutine
            if mainMenu == "1": # if the user input equals to the first item or option in the list ["1", "2", "3", "4", "5"]:
                readFilm.printData() # invoke or call the filename.subroutine
            elif mainMenu == "2":
                addFilm.film()
            elif mainMenu == "3":
                updateFilm.update()
            elif mainMenu == "4":
                deleteFilm.delete()
            else:
                mainProgram = False
    elif opt == "2":            
        while mainProgram == True: #check/compare that main program equals to true
            reportMenu = reportOptions() # we passed in the menuOptions() function to the variable mainmenu
            if reportMenu == "1": # if the user input equals to the first item or option in the list ["1", "2", "3", "4", "5"]:
                readFilm.printData() # invoke or call the filename.subroutine
            elif reportMenu == "2":
                report.filmGenre()
            elif reportMenu == "3":
                report.filmYear()
            elif reportMenu == "4":
                report.filmRating()
            else:
                mainProgram = False
    elif opt == "3":
        mainProgram = False
    else:
        print("Invalid Option Choosen")
        



