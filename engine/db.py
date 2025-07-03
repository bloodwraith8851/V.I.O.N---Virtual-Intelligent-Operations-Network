import sqlite3

conn = sqlite3.connect('vion.db')
cursor = conn.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES (null, 'Android studio', 'C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe')"
# cursor.execute(query)
# conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null, 'Youtube', 'https://www.youtube.com/')"
# cursor.execute(query)
# conn.commit()





# cursor.execute("DELETE FROM sys_command WHERE id = ?", (4,))

# conn.commit()
# conn.close()