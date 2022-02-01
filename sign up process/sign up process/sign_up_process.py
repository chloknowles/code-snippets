### SIGN UP PAGE ###

### Creates an account ###
def sql_createacc(entities): #CREATE ACCOUNT
    conn = sqlite3.connect('fitness_database.db')
    cursorObj = conn.cursor()
    create_query = "INSERT INTO fitness_users (Email_address, User_name, User_password, Premium_member) VALUES (?,?,?,?)"
    cursorObj.execute(create_query, entities)
    conn.commit()

def signup_process(): ### Process for creating an account ###
    global stored_userid ## global variable used again
    global premium_user
    EmailA = signup_textbox_email.value
    NameUser = signup_textbox_username.value
    Pword = signup_password_textbox.value
    Prem = signup_premium_checkbox.value
    print (Prem)
    premium_user = 0
    if EmailA == "" or NameUser == "" : 
        info("ERROR","All details must be entered")
    elif len(Pword) < 5:
        info("ERROR","Pasword must be atleast 5 characters long")
    elif '@' not in EmailA:
        info("ERROR", "Please enter a valid email.")
    elif Prem == 1:
        premium_user = 1
    elif Prem == 0:
        premium_user = 0

    # insert user as all credential correct
    entities = (EmailA,NameUser, Pword, premium_user)
    sql_createacc(entities)
    info("INSERT USER","Account Created")
     ### set up SQL to find new user on the database ###
    sqlselect = "SELECT * FROM fitness_users WHERE Email_address = '"+ EmailA +"'"
    rows = query_database(database_file, sqlselect)
    if len(rows) == 0: ### This checks that the user was found ###
        info("Error","New user not found")
    else:
        ### Stored UserID is stored as rows[0,0]
        stored_userid = (rows[0][0])  
        storedemail = (rows[0][1])
        if premium_user == 1:
            open_premium()
        elif premium_user == 0:
            open_standard()
