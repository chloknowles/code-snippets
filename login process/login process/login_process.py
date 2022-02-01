def login_process(): ### Login form validation and checks email and password ###
    global stored_userid ## variable needed in all forms ##
    global premium_user
    if username_textbox.value == " ":
        info("Error", "You must enter a valid username")
    elif password_textbox.value == " ":
        info("Error", "You must enter a password")

    else:
        username = username_textbox.value
        password = password_textbox.value
        ### set up SQL to find username on the database ###
        sqlselect = "SELECT * FROM fitness_users WHERE User_name = '"+username+"'"
        rows = query_database(database_file, sqlselect)
        if len(rows) == 0: ### This checks that the user was found ###
            info("Error","Error")
        else:
            ### Stored UserID is stored as rows[0,0]
            stored_userid = (rows[0][0])  # We need this as a foreign key
            storedusername = (rows[0][2])
            storedpassword = (rows[0][3])
            premium_user = (rows[0][4])
            if username == storedusername and password == storedpassword:
                info("Log in","Success")
                if premium_user == 1:
                    open_premium()
                elif premium_user == 0:
                    open_standard()
            else:
                info("Error","Incorrect")


login_window = Window(app, title="Login")
login_window.hide()
text_blank = Text(app, text=" ")
text_blank = Text(app, text=" ")
login_title = Text(login_window, text ="Login")
login_title.text_size = 20
text_username = Text(login_window, text="Enter Username:")
text_username.text_color = "black"
username_textbox = TextBox(login_window, width = 20)
username_textbox.bg = "white"
text_password = Text(login_window, text="Enter Password:")
text_password.text_color = "black"
password_textbox = TextBox(login_window, hide_text=True, width = 20)
password_textbox.bg = "white"
button_login = PushButton(login_window, text = "Log in", command = login_process)

