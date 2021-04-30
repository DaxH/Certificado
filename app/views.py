from django.shortcuts import render,redirect
import firebase_admin
from django.conf import settings
from firebase_admin import firestore
# Create your views here.
def index(request):
    print(f"FIREBASE CONFIG {settings.FIREBASE_CONFIG}")
    if not firebase_admin._apps:
        firebase = firebase_admin.initialize_app(settings.FIREBASE_CONFIG)
    db = firestore.Client()
    print(f"FIREBASE {db}")
    return render(request,'app/index.html')
