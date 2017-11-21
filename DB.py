import sqlite3

conn = sqlite3.connect('database.sqlite3')
cur = conn.cursor()

conn.execute('''CREATE TABLE LICENSE
         (NUMBER  CHAR(50)     NOT NULL,
         NAME           TEXT    NOT NULL,
         PHONE            CHAR(13)     NOT NULL,
         ADDRESS        CHAR(50));''')
#print "Table created successfully";

conn.execute("INSERT INTO LICENSE (NUMBER,NAME,PHONE,ADDRESS) \
      VALUES ('KL42654', 'Abhishek', '+919048881192', 'EC HOUSE')");

conn.execute("INSERT INTO LICENSE (NUMBER,NAME,PHONE,ADDRESS) \
      VALUES ('A350225', 'Adarsh', '+918129151294', 'EC HOUSE')");

conn.execute("INSERT INTO LICENSE (NUMBER,NAME,PHONE,ADDRESS) \
      VALUES ('KL42844', 'Christy', '+919633696393', 'EC HOUSE')");

conn.execute("INSERT INTO LICENSE (NUMBER,NAME,PHONE,ADDRESS) \
      VALUES ('KL42845', 'Abhishek', '+919497652624', 'EC HOUSE')");

conn.commit()
print "Records created successfully";

cursor = conn.execute("SELECT NUMBER, NAME, PHONE, ADDRESS from LICENSE")
for row in cursor:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully";

conn.close()
