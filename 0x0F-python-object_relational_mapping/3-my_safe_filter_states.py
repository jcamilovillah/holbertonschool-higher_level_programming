#!/usr/bin/python3

""" SQL injections safe
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    userr = argv[1]
    passw = argv[2]
    namd = argv[3]
    match = argv[4]
    lc = "localhost"

    db = MySQLdb.connect(host=lc, port=3306, user=userr, passwd=passw, db=namd)
    cur = db.cursor()
    exe = cur.execute("SELECT * FROM states WHERE name=%s\
                    ORDER BY id;", (match,))
    for x in cur.fetchall():
        print(x)
    db.close()
    cur.close()
