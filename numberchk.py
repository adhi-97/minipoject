import sqlite3
import os
from twilio.rest import Client
import pyrebase
import subprocess

process = subprocess.Popen(['alpr', '/root/Desktop/lp.jpeg'],stdout=subprocess.PIPE)
for i in range(8,10):
	output = process.stdout.readline()
	process.poll()
print output[6:15]

conn = sqlite3.connect('database.sqlite3')
cur = conn.cursor()
cursor = conn.execute("SELECT NUMBER, NAME, PHONE, ADDRESS from LICENSE")

c=output[6:15]

for row in cursor:
	if(row[0] in c):
		print "liscence found = ",row[0];
		Number=row[0];
		Name=row[1];
		phone=row[2];
		Address=row[3];
		print phone;
		
		account_sid = "AC59f6df9e8f6d59670f321fba9f9ed933"
		auth_token = "85c71194c1e949713c273759629aaa58"
		
		client = Client(account_sid, auth_token)

		client.messages.create(
		    to=phone,
		    from_="+447492888196",
		    body="Your car is in non parking zone dude")

		config = {
		  "apiKey": "AIzaSyDEkAQcf10kaJNL2AIttWIJrWf37yl7fEA",
		  "authDomain": "AIzaSyDEkAQcf10kaJNL2AIttWIJrWf37yl7fEA",
		  "databaseURL": "https://licenseplatedetector.firebaseio.com",
		  "storageBucket": "licenseplatedetector.appspot.com",
		  "serviceAccount": "/root/Desktop/licenseplatedetector-firebase-adminsdk-vv11r-a6a84c540e.json"
		}

		firebase = pyrebase.initialize_app(config)
		db = firebase.database()
		db.child("users").child("2")
		data={"License No":Number , "Name" :Name ,"Phone":phone,"Address":Address}
		db.set(data)
print "done";





	
