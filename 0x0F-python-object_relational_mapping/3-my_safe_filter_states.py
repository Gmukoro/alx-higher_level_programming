#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument (safe from SQL injectn)
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curso = db.cursor()
    match = sys.argv[4]
    curso.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = curso.fetchall()
    for row in rows:
        print(row)
    curso.close()
    db.close()
