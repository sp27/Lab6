import MySQLdb
conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="wine")
x = conn.cursor()

try:
       x.execute("SELECT * FROM vineyard")
       print "Getting data from vineyard table :"
       results = x.fetchall()
       for row in results:
          fname = row[0]
          lname = row[1]
          
       print "vineyardID=%d,vineyardName=%s" % \
             (fname, lname)
       conn.commit()
except:
       conn.rollback()

conn.close()