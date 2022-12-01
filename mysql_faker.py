# using faker library inserting fkae email time into mysql database
import os
import time
import random 
from datetime import datetime, timedelta
import datetime
from faker import Faker
Faker.seed(365456)
fake = Faker()

#mysql connection
import mysql.connector
myconnection = mysql.connector.connect(host ="localhost",user="root",passwd="password",database="join_us")
mycursor = myconnection.cursor()


buss = []
n = 100
for i in range(0,n):
    now = fake.date_time()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    row = [fake.email()]
    print(formatted_date)

    print(row)
    
    
    mycursor.execute(' INSERT INTO users (email,created_at)  VALUES ("%s","%s") ' %(row[0],formatted_date)) 

myconnection.commit()
