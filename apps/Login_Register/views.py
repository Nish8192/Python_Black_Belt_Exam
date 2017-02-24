from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import User
import bcrypt
from django.contrib import messages
from datetime import datetime
# Create your views here.

def index(request):
    if 'log_user_id' not in request.session:
        request.session['log_user_id'] = 0
        request.session['log_user_name'] = ''
    context = {
    'messages': messages.get_messages(request)
    }
    return render(request, 'Login_Register/index.html', context)

def createUser(request):
    if request.method == 'POST':
        flag = True
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email_address']
        pw = str(request.POST['pw'])
        pwc = str(request.POST['pwc'])

        bday = datetime.strptime(str(request.POST['birthday']), '%Y-%m-%d')
        print bday

        users = User.objects.filter(email=email)
        if not users:
            if not User.objects.validName(first_name):
                messages.error(request, 'First Name must be at least three characters')
                flag = False
            if not User.objects.validName(last_name):
                messages.error(request, 'Last Name must be at least three characters')
                flag = False
            if not User.objects.validateEmail(email):
                messages.error(request, 'Please enter a valid email address')
                flag = False
            if not User.objects.validPassword(pw):
                messages.error(request, 'Please enter a valid password, at least 8 characters long, using letters, numbers, or special characters (@#$%^&+=)')
                flag = False
            if not User.objects.confirmPassword(pw, pwc):
                messages.error(request, 'The entered passwords do not match')
                flag = False
            if not User.objects.oldEnough(bday):
                messages.error(request, 'You are not old enough to create an account with us :(')
                flag = False
            if flag:
                hashed = bcrypt.hashpw(pw, bcrypt.gensalt())
                user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=hashed, birthday=bday)
                request.session['log_user_id'] = user.id
                request.session['log_user_name'] = user.first_name
                request.session['log_user_alias'] = user.alias
                return redirect(reverse('travel_dashboard:index'))
        else:
            messages.error(request, 'This email address is already registered, please log in below!')
    return redirect('/')

def logOut(request):
    request.session.clear()
    return redirect('/')

def logIn(request):
    if request.method == 'POST':
        email = request.POST['email_address']
        password = str(request.POST['pw'])
        users = User.objects.filter(email=email)
        if not users:
            messages.error(request, 'This user does not exist!')
            return redirect('/')
        for user in users:
            if bcrypt.hashpw(password, str(user.password)) == str(user.password):
                request.session['log_user_id'] = user.id
                request.session['log_user_name'] = user.first_name
                return redirect(reverse('travel_dashboard:index'))
            else:
                messages.error(request, 'Sorry, invalid password')
                return redirect('/')

    return redirect('/')
