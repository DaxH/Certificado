from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import firestore
# Create your views here.
def index(request):
    if not firebase_admin._apps:
        firebase = firebase_admin.initialize_app()
    db = firestore.Client()
    print(db)
    return render(request,'app/index.html')
