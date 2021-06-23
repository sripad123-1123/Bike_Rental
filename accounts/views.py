from bike_rental.settings import EMAIL_HOST_USER
from email.mime import text
from django.http import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Account, profile_verify

from django.contrib.auth import get_user_model
# from django_email_verification import sendConfirm
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
import uuid



# Create your views here.

def login(request):
    # print("Inside login")
    if request.method == 'POST':
        # print("Inside login post")
        username = request.POST['username']
        password = request.POST['password']
       
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            profile_obj = profile_verify.objects.filter(user1 = user).first()

            if not profile_obj.is_verified:
                messages.info(request,"Your account is not verified kindly verify!")
                return redirect('login')
            
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


def register(request):

    if request.method == 'POST':
       
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if Account.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')

            else:
                user = Account.objects.create_user(first_name = first_name,last_name=last_name, email = email, password = password1)
                user.save()

                auth_token1 = str(uuid.uuid4())
                profile_obj = profile_verify.objects.create(user1 = user, auth_token = auth_token1 )
                profile_obj.save()
                send_mail_after_reg(email, auth_token1)
                return redirect('token_send')

        else:
            messages.info(request,'Password and Confirm Password are not matching')
            return redirect('register')
    #return redirect('/')

        
       

    else:
        return render(request,'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

def token_send(request):
    return render(request,'token_send.html')


def success(request):
    return render(request,'success.html')

def send_mail_after_reg(email, token):
    subject = 'Your account needs to be verified'
    message = f'please click the link to verify your account http://127.0.0.1:8000/accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    mail1 = EmailMessage(subject, message, email_from, recipient_list)
    mail1.send(fail_silently=False)

def verify(request,token):
    profile_obj = profile_verify.objects.filter(auth_token = token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.info('Your account has been verified.')
            return redirect('login')
        
        profile_obj.is_verified = True
        fname = profile_obj.user1.first_name
        profile_obj.save()
        messages.info(request,'Your account has successfully been verified')
        text = f'Hey {fname} !Your account has successfully been verified!'

        email2 = EmailMessage(
            "Get 'n' Ride registration confirmation!",
            text,
             
            settings.EMAIL_HOST_USER,
            {profile_obj.user1.email},
        )
        email2.send(fail_silently=False)
        return redirect('login')

        
        






    
