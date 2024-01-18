from django.shortcuts import render
# from pyrebase_settings import db, authw
from django.shortcuts import render
import pyrebase

config={
    "apiKey": "AIzaSyBIGqrQdwFmhSa0wMtmdcpXPZLn_bJUbKw",
    "authDomain": "jarvis-hackathon-e2787.firebaseapp.com",
    "projectId": "jarvis-hackathon-e2787",
    "databaseURL": "https://jarvis-hackathon-e2787-default-rtdb.firebaseio.com",
    "storageBucket": "jarvis-hackathon-e2787.appspot.com",
    "messagingSenderId": "524606379922",
    "appId": "1:524606379922:web:9050c09c1fe2142b5c134b"
}
firebase=pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()

def index(request):
    return render(request, 'index.html')

def options(request):
    return render(request, 'options.html')

def tPro(request):
    return render(request, 'tPro.html')

def lPro(request):
    return render(request, 'lPro.html')

def tDash(request):
    return render(request, 'tDash.html')

def lDash(request):
    return render(request, 'lDash.html') 

def get_users(request):
    users = db.child("users").get()
    return render(request, 'users.html', {'users': users.val()})