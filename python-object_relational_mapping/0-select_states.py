#!/usr/bin/env python3
import MySQLdb
import sys

def main(user, password, database):

    mydb = MySQLdb.connect(host='localhost',port=3306, user=user, passwd=password, db=database)
    mycur = mydb.cursor()
    mycur.execute('select * from states')

    for i in mycur:
        print(i)

    if mydb in locals() and mydb.is_connected():
        mycur.close()
        mydb.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
