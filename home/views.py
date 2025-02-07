from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request, 'about.html')


def fruit(request):
    return render(request, 'fruit.html')

def contact(request):
    return render(request, 'contact.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def login_view(request):
    return render(request, 'login.html')





def auth_page(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect authenticated users to the home page

    login_form = AuthenticationForm()
    signup_form = UserCreationForm()

    if request.method == "POST":
        if 'login' in request.POST:
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('index')  # Redirect after successful login

        elif 'signup' in request.POST:
            signup_form = UserCreationForm(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                return redirect('index')  # Redirect after successful signup

    return render(request, 'auth.html', {'login_form': login_form, 'signup_form': signup_form})
