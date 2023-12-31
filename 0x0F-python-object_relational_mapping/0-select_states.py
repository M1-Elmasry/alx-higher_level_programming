#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb


if __name__ == "__main__":
    con = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8",
        port=3306,
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    con.close()
