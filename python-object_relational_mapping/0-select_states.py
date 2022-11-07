#!/usr/bin/python3
"""
    Importing the MySQLdb module and the sys module. It is then connecting to\
        the database and creating a cursor. It is then executing the query and\
            printing the results.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
