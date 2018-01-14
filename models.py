import sqlite3 as sql


def insert_data(query, response, timest):
    con = sql.connect('database.db')
    print("Opened database successfully");
    cur = con.cursor()
    cur.execute("INSERT INTO chat(query, response, dated) VALUES (?,?,?)", (query, response, timest))
    con.commit()
    print("Record added successfuly.")
    con.close()


def retrieve_data():
	con = sql.connect('database.db')
	print("Opened database2 successfully")
	cur = con.cursor()
	cur.execute("SELECT * FROM chat")
	x = [dict((cur.description[i][0], value)
		for i, value in enumerate(row)) for row in cur.fetchall()]
	con.close()
	return x


