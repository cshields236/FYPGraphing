import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from matplotlib import pyplot as plt

cred = credentials.ApplicationDefault()
faces = []
f = []

rightEyes = []
leftEyes = []
times = []



cred = credentials.Certificate("C:/Users/Conor's Laptop/Downloads/FYPFirebaseProject-fbd67ba91d2b.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


users_ref = db.collection(u'users/icUjM6Fm4oQignPP3FgWFBgsERs2/Journeys')
docs = users_ref.stream()

for doc in docs:
    faces.append(doc.to_dict())
    
for face in faces:
    f.append(face['journeyInformationss'])

# print(f[365])
for i in range(len(f)):
    rightEyes.append(f[i][0]['rightEye'] * 100)
    leftEyes.append(f[i][0]['leftEye'] * 100)
    times.append(f[i][0]['time'].split(" ")[1])

times.sort()


print (times[1])
print (times[len(times)-1])
plt.style.use('fivethirtyeight')
plt.title('Blinking Patterns')
plt.ylabel('Eye Open %')
plt.xlabel('Time')
plt.plot(times, rightEyes,color='b', label = 'Right Eye')
plt.plot(times, leftEyes,color = 'k' , label = 'Left Eye')
plt.legend()
plt.show()