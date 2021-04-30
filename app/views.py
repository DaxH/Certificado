from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore
# Create your views here.
def index(request):
    if not firebase_admin._apps:
        firebase = firebase_admin.initialize_app()
    db = firestore.Client()
    collection = db.collection('Collection Python')
    response = collection.stream()
    response_dict = {data.id:data.to_dict() for data in response}
    data = [{
    'response':response_dict
    }]
    print(data)
    return render(request,'app/index.html')
