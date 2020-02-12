import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.ApplicationDefault()
faces = []

cred = credentials.Certificate("C:/Users/Conor's Laptop/Downloads/FYPFirebaseProject-fbd67ba91d2b.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


users_ref = db.collection(u'users/oW2ia7qAHWdxwVhpN1g8xaufKKx1/Journeys')
docs = users_ref.stream()

for doc in docs:
    # print(u'{} => {}'.format(doc.id, doc.to_dict()))
    faces.append(doc.to_dict())

print (faces[2])

