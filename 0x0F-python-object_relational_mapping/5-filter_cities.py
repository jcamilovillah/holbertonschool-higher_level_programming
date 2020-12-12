#!/usr/bin/python3
""" script that list states
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    userr = argv[1]
    passw = argv[2]
    namd = argv[3]
    state_name = argv[4]
    lc = "localhost"

    db = MySQLdb.connect(host=lc, port=3306, user=userr, passwd=passw, db=namd)
    cur = db.cursor()
    exe = cur.execute("SELECT cities.name FROM cities JOIN states\
        ON cities.state_id=states.id\
        WHERE states.name= % s ORDER BY cities.id", (state_name,))
    comma = ""
    for row in cur.fetchall():
        for col in row:
            print("{}{}".format(comma, col), end="")
            comma = ", "
    db.close()
    cur.close()
