from django.shortcuts import render, redirect
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def quotes(request):
    return render(request, 'login/success.html')

def login_user(request):
    login = User.objects.login_user(request.POST)
    if login[0]:
        request.session['user_id'] = login[1].id
        name = User.objects.get(id = 'user_id')
        return redirect('/quotes')
    return redirect('/')

def create_user(request):
    #used to validate and create a new user
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt()),
        )
        request.session['user_id'] = user.id
        return redirect('/quotes')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def submit_quote(request):
    if Quote.objects.validate_quote(request.POST):
        quote = Quote.objects.create(
        author = request.POST.get('author'),
        message = request.POST.get('message'),
        )

def show(request, user_id):
    context = {

    }

    return render(request, 'login/aboutuser.html')
