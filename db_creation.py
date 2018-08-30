# db creation script
import sqlite3

# this creates db in the current working directory
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# create table if not exists
c.execute('''DROP TABLE IF EXISTS tasks;''')
c.execute('''
	CREATE TABLE IF NOT EXISTS tasks 
	(ID INTEGER PRIMARY KEY AUTOINCREMENT, 
	NAME TEXT NOT NULL,
	DESCRIPTION TEXT NOT NULL,
	STATUS TEXT NOT NULL);''')

# insert two test values
c.execute('''
	INSERT INTO tasks VALUES (NULL, ?, ?, ?)''', ('sample_task', 'sample description', 'not done'))
c.execute('''
	INSERT INTO tasks VALUES (NULL, ?, ?, ?)''', ('another sample task', 'another sample description', 'woohoo not done'))
conn.commit()