import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("../serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def is_rick_roll(url):
    if is_in_db(url):
        return True

def is_in_db(user_url):
    urls = db.collection('rickroll').document('urls').get().to_dict()
    for url in urls:
        if url in user_url:
            return True
    return
