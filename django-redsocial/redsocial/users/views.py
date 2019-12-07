from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('post')
        else:
            return render(request, 'user/login.html', {'error': 'invalid username or password'})
    return render(request, 'user/login.html', {'post': 'users'})


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        passwordconfirm = request.POST['passwordconfirm']

        if password != passwordconfirm:
            return render(request, 'user/signup.html', {'errorsignup': 'errorr passw'})

        usersing = User.objects.create_user(username=username, password=password)
        usersing.firstname = request.POST['firstname']
        usersing.lastname = request.POST['lastname']
        usersing.email = request.POST['email']
        profile = Profile(user=usersing)
        # otra forma de guardar Profile.objext.create()
        profile.save()

        return redirect('login')
    return render(request, 'user/signup.html')