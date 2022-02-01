### Run a query to SELECT ###
def query_database(database, query):
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    return rows


