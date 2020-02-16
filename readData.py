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


users_ref = db.collection(u'users/oW2ia7qAHWdxwVhpN1g8xaufKKx1/Journeys')
docs = users_ref.stream()

for doc in docs:
    faces.append(doc.to_dict())
    
for face in faces:
    f.append(face['journeyInformationss'])

# print(f[365])
for i in range(30):
    rightEyes.append(f[i][0]['rightEye'] * 100)
    times.append(f[i][0]['time'].split(" ")[1])



plt.title('Blinking Patterns')
plt.ylabel('Eye Open %')
plt.xlabel('Time')
plt.plot(times, rightEyes)
plt.show()