#!/usr/bin/python3
""" script that list states
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    userr = argv[1]
    passw = argv[2]
    namd = argv[3]
    lc = "localhost"

    db = MySQLdb.connect(host=lc, port=3306, user=userr, passwd=passw, db=namd)
    cur = db.cursor()
    exe = cur.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN\
        states ON cities.state_id=states.id ORDER BY cities.id")
    for x in cur.fetchall():
        print(x)
    db.close()
    cur.close()
