from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


# Create your views here.
def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('post')
        else:
            return render(request, 'user/login.html', {'error': 'invalid username or password'})
    return render(request, 'user/login.html', {'post': 'users'})

