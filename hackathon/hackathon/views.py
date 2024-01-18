from django.shortcuts import render
# from pyrebase_settings import db, authw
from django.shortcuts import render
import pyrebase

config = {
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


def render_login_page(request):
    return render(request, 'login.html')


def get_users(request):
    users = db.child("users").get()
    return render(request, 'users.html', {'users': users.val()})


def post_sign_in(request):
    tenant_email = request.POST.get('email')
    tenant_password = request.POST.get('password')

    try:
        user = auth.sign_in_with_email_and_password(
            email=tenant_email,
            password=tenant_password
        )

    except:
        error_message = "Invalid Credentials. Please try again."
        return render(
            request,
            template_name="login.html",
            context={"message": error_message}
        )

    session_id = user['idToken']
    print(session_id)
    # request.session['uid'] = str(session_id)

    return render(
        request,
        template_name="login_success.html",
        context={"email": tenant_email}
    )


def logout(request):
    del request.session['uid']
    return render(request=request, template_name="index.html")


def post_sign_up(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    print("Email: " + email)
    print("Password: " + password)

    user = auth.create_user_with_email_and_password(email, password)
    uid = user['localId']
    print(user)
    id_token = request.session['uid']
    print(uid)

    return render(request, "register_success.html")


def render_register_page(request):
    return render(request=request, template_name='register.html')
