################################################
# Database name (global variable)
database_file = 'fitness_database.db'
# Delete the database
if os.path.exists(database_file):
    os.remove(database_file)

# Connect to the database
conn = sqlite3.connect(database_file)
# Get a cursor pointing to the database
cursor = conn.cursor()
# Create the tables
cursor.executescript(sql)
# Commit to save everything
conn.commit()
# Close the connection to the database
#################################################

