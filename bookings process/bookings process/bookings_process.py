def openbooking_process(): ### Process for opening your bookings ###
    global stored_userid
    info("My Bookings","Directing you to your Bookings..",)
    ###
    ## Look at your bookings
    sqlselect = "SELECT * FROM Bookings WHERE UserID = "+ str(stored_userid)+ ""
    rows = query_database(database_file, sqlselect)
    numrows = len(rows)
    if len(rows) == 0: ### This checks that the user was found ###
        info("Error","No bookings found")
    else:
        for row in range(numrows):
           numG = (rows[row][2])
           dateb = (rows[row][3])
           timeb = (rows[row][4])
           detail = ("       "+ str(numG) + "              " + dateb + "         " + str(timeb) )
           listbox_booking.insert(row,detail)
        
    windowN.show()


def booking_createprocess():
    global stored_userid #This has been stored from the database
    info("Booking","Booking Confirmed")
    windowB.show()
    if inputguestbox.value == "" : 
         info("ERROR","Booking details must be entered")
    
    else:
        
        # insert booking correct
        Numberof_guests = inputguestbox.value
        Dateof_vist = inputdatebox.value
        Timeof_visit = inputtimebox.value
        UserID= stored_userid
        User_requests = "Vegan"
        entitiesB = (UserID, Numberof_guests, Dateof_vist, Timeof_visit, User_requests)
        sql_createbooking(entitiesB)
        #info("INSERT NOTE","Note added")
    


### VIEW BOOKINGS PAGE ###
titlebooking = Text(windowN, text = "My Bookings")
titlebooking.text_size = 20
guestbox = Text(windowN, text = "Number of guests   Date of visit         Time of visit   User requests")


listbox_booking = ListBox(windowN, items=[""],height = 60, width = 400, scrollbar = True)
listbox_booking.text_size = 13
app.display()
