#!/usr/bin/python3
""" script that lists all cities and states with left join
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    userr = argv[1]
    passw = argv[2]
    namd = argv[3]
    sta_nme = argv[4]
    lc = "localhost"

    db = MySQLdb.connect(host=lc, port=3306, user=userr, passwd=passw, db=namd)
    cur = db.cursor()
    exe = cur.execute("SELECT cities.name FROM cities JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id;", (sta_nme,))
    content = cur.fetchall()
    i = 1
    size = len(content)
    for a in content:
        if i != size:
            print('{}, '.format(a[0]), end='')
        else:
            print(a[0])
        i += 1
    db.close()
    cur.close()
