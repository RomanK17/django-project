from django.shortcuts import render
from django.contrib import auth

from users.form import UserLoginForm

# Create your views here.

def log(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request,user)
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)

def reg(request):
    return render(request, 'users/register.html')
