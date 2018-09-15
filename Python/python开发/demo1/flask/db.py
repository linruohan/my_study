import MySQLdb

conn=MySQLdb.connect("localhost","root","12345","news")
cur=conn.cursor()


def addUser(username,password):
    sql="insert into user (username,password) values('%s','%s')"%(username,password)
    cur.execute(sql)
    conn.commit()
    conn.close()
