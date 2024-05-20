from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib import sessions

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['uname'] = str(request.user)
            return redirect('home')
        else: 
            messages.warning(request, "Login failed")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, 'Registration success')
            return redirect('login')
        else:
            messages.error(request, "Form field is invalid")
    else:
        form = RegisterUserForm()
        return render(request, 'register.html', {'form': form})
    messages.warning(request, "Registration failed")
    return redirect('register')

def logout_user(request):
    logout(request)
    return redirect('home')