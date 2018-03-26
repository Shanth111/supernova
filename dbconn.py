import MySQLdb

def connection():
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='supernova',
                           db='rdata')
    rd = conn.cursor()
    return rd,conn
    