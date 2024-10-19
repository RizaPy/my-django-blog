from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth     import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .forms import LoginForm, RegisterForm 

class RegisterView(View):
    def get(self, request):
        create_form = RegisterForm()
        context = {
            'form':create_form
        }
        return render(request, 'users/register.html', context)
    
    def post(self, request):
        create_form = RegisterForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('login') 
        else:
            context = {
            'form':create_form
        }

        return render(request, 'users/register.html', context)
    
class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'form':login_form
        }
        return render(request, 'users/login.html', context)
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')

        else:
            context = {
                'form':login_form
            }
            return render(request, 'users/login.html', context)



def user_logout(request):
    logout(request)
    return redirect('home')
    
