import sqlite3

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)

	return None

def create_country(conn, country):
	sql = ''' INSERT INTO countries(name)
						VALUES(?) '''
	cur = conn.cursor()
	cur.execute(sql, country)
	return cur.lastrowid

def create_city(conn, city):
	sql = ''' INSERT INTO cities(name, )
						VALUES(?) '''
	cur = conn.cursor()
	cur.execute(sql, city)
	return cur.lastrowid