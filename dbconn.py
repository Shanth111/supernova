import MySQLdb

def connection():
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='icantTellu@25',
                           db='rdata')
    rd = conn.cursor()
    return rd,conn
    