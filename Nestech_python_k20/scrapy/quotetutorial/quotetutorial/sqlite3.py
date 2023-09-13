import _sqlite3
import os

path = os.path.dirname(__file__)
path_out = os.path.join(path,"mysqlite3.db")

conn = _sqlite3.connect(path_out)
curr = conn.cursor()
print(curr)
curr.execute("""create table quotes_tb(
    title text,
    author tex,
    tag text
    )""")
conn.commit()
conn.close()