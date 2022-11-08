#!/usr/bin/python3
"""
    Script that takes in the name of a state as an argument\
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities LEFT\
        JOIN states ON states.id = cities.state_id WHERE\
        BINARY states.name = %(name)s", {
            'name': sys.argv[4]
        })
    rows = cur.fetchall()
    for idx, row in enumerate(rows):
        print(row[1], end="" if idx == (len(rows) - 1) else ", ")
    print()
