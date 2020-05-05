import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from matplotlib import pyplot as plt
import matplotlib as mpl
import datetime as dt
import numpy as np

cred = credentials.ApplicationDefault()
faces = []
f = []
final = []
pfinal = []
rightEyes = []
leftEyes = []
times = []
blinks = []

cred = credentials.Certificate("C:/Users/Conor's Laptop/Downloads/FYPFirebaseProject-fbd67ba91d2b.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# get the specific journey 
users_ref = db.collection(u'users/1gsLjv0VLbSqKahPDB1lpEgtgck1/Journeys/2020-04-21 09:44:01/Journey')
docs = users_ref.stream()

    
for doc in docs:
    faces.append(doc.to_dict())
    
#find the specific journeys information 
for face in faces:
    f.append(face['journeyInformationss'])
    
for info in f:
    final.append(info)

for i in range(len(final)):
    for l in final[i]:
        pfinal.append(l)

# traverse list to break down into lists for both eyes and the times
for i in range(len(pfinal)):
    rightEyes.append(pfinal[i]['rightEye'] * 100)
    leftEyes.append(pfinal[i]['leftEye'] * 1000)
    r = pfinal[i]['time'].split(" ")[1]
    times.append(dt.datetime.strptime(r, r'%H:%M:%S'))

# find numbers of binks at 10% treashold 
b=0
for r in rightEyes:
    if r < 10:
        b += 1
        blinks.append(b)
    else: 
        blinks.append(b)



# graph the values 
times.sort()
dates = mpl.dates.date2num(times)




plt.title('10% Threshold')
plt.ylabel('Eye Open %')
plt.xlabel('Time')

plt.plot_date(times, blinks, 'b-', label = 'Blinks')
plt.plot_date(dates, rightEyes,'b-' ,color='k', label = 'Eyes Open Probability %') 
plt.legend()

plt.show()

