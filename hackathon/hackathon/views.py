from django.shortcuts import render
# from pyrebase_settings import db, authw
from django.shortcuts import render
import firebase_admin
# from firebase_admin import storage
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
auth=firebase.auth()
db=firebase.database()
# ref = db.reference("/")

def index(request):
    return render(request, 'index.html')

def tPro(request):
    return render(request, 'tPro.html')


def upload_tenant_info(request):
    temp = db.child('landlords').get().val()
    # ref = db.reference("/") 

    # db.ref('landlords', None, params=filter_condition)
    
    data_to_push = {
        'name': request.POST.get('name'),
        'address': request.POST.get('currentAddress'),
        'city': request.POST.get('city'),
        'contact': request.POST.get('phoneNumber'),
        'criminal_record': request.POST.get('criminalRecord'),
        'credit_score': request.POST.get('creditScore'),
        'profession': request.POST.get('profession'),
        'dependents': request.POST.get('dependents'),
        'pets': request.POST.get('pets'),
        'vehicles': request.POST.get('numVehicles'),
        # 'userId': auth.current_user['localId']
        'userId': 'IOX0zxHMtEWLtS8yNjmKAJuFjUX2'
    }

    db.child("tenants").push(data_to_push)

    return render(request, 'uploaded.html')

def get_tenant_info(request):
    # users = db.child("users").get()
    # query_owner_id = client.query(kind="Photo", filters=[("owner_id", "=", "user1234")])
    temp = db.child('landlords').get().val()
    # ref = db.reference("/") 

    # db.ref('landlords', None, params=filter_condition)
    
    data_to_push = {
        'name': 'Example Name',
        'address': 42,
        'contact': "905-485-5233",
        'dependents': False,
        'income': 51000,
        'pets': False,
        'vehicles': 0,
    }

    # data_for_landlords = {
    #     'applied': 
    # }

    # db.child("tenants").push(data_to_push)
    # db.child("tenants").update(data_to_push)

    # db.child("landlords").order_by_child('')


    # UPLOAD
    # storage = firebase.storage()
    # storage.child("hello.txt").put('hello.txt')

    return render(request, 'tenant_form.html', {'tenants': temp })


def upload_file(request):
    # Initialize Firebase Admin SDK
    # cred = credentials.Certificate('path/to/your/firebase/credentials.json')
    # firebase_admin.initialize_app(cred, {'storageBucket': 'your-firebase-project-id.appspot.com'})
    bucket = firebase.storage.bucket()

    if request.method == 'POST' and request.FILES['file']:
        # Get the file from the request
        file = request.FILES['file']

        # Generate a unique filename or use the original filename
        filename = default_storage.get_available_name(file.name)

        # Upload the file to Firebase Storage
        blob = bucket.blob(filename)
        blob.upload_from_string(file.read(), content_type=file.content_type)

        # Optionally, store file information in the Firebase Realtime Database
        # db = firebase.FirebaseApplication('https://your-firebase-project-id.firebaseio.com/', None)
        file_data = {'filename': filename, 'download_url': blob.public_url}
        db.post('/uploaded_files', file_data)

        return JsonResponse({'status': 'File uploaded successfully', 'download_url': blob.public_url})

    return render(request, 'upload_file.html')
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
