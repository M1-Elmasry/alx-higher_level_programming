#!/usr/bin/python
"""
script that lists all states in states table
from the database hbtn_0e_0_usa in ascending order
"""
from sys import argv
import MySQLdb


def list_states(host="localhost", user=argv[1], passwd=argv[2], db=argv[3]):
    """
    lists all states in states table
    from the database hbtn_0e_0_usa in ascending order
    """
    con = MySQLdb.connect(
        host=host, user=user, passwd=passwd, db=db, charset="utf8"
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    list_states()
