from datetime import datetime
from email import message
import string
from django.conf import settings
from django.shortcuts import redirect, render
from httplib2 import Authentication
from myapp.models import Signup,qur
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import datetime




def signup(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        dob=request.POST.get('dob')
      
        user = Signup(username=username, password=password,email=email,dob=dob)
        mydict={'username':username}
        user.save()

        send_mail(
             'Congratulations Mail',
            'Your account successfully Created',
            'chiragsaxena001@gmail.com',
            ['chiragsaxena001@gmail.com'],
            fail_silently=False,
        )
    
        return redirect('signin')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            d1 = Signup.objects.get(username=username, password=password)
        except Signup.DoesNotExist:
            return render(request, 'signin.html')
        else:
            request.session['uid'] = d1.id
            return redirect("profile")
    else:
        return render(request, 'signin.html')

def profile(request):
    return render(request, 'profile.html')

def logout(request):
    return render(request,'logout.html')    

def faq(request):
    return render(request,'faq.html')    

def services(request):
    return render(request,'services.html')    



def contact(request):
    uiid=request.session.get('uid')
    if request.method =='POST':
       data1=request.POST.get('nm','')    
       data2=request.POST.get('em','')  
       data3=request.POST.get('sb','')  
       data4=request.POST.get('ms','')  
       song_obj = qur(uid=uiid, username = data1, email=data2, subject = data3, message = data4)  
       song_obj.save()
       subject = data3
       message = data4
       email_from = data2
       recipient_list = ['chiragsaxena001@gmail.com']
       #send_mail(subject, message,email_from, recipient_list )
       send_mail(subject, message, email_from, recipient_list)
       return redirect("signup")
    return render(request,'contact.html',{})

def home(request):
    return render(request,'home.html')    

def about(request):
    return render(request,'about.html')

def date_time_view(request):
    date=datetime.datetime.now()    

