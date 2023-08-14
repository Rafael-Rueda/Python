from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth import logout as user_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from apps.authors import forms


def login(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user is not None:
                user_login(request, user)
                return redirect('/')
            else:
                return redirect('authors:login')
    return render(request, 'authors/pages/login.html', {'form': form})

def register(request):
    form = forms.RegisterForm(request.session.get('data_form'))
    if 'data_form' in request.session:
        del(request.session['data_form'])

    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        request.session['data_form'] = request.POST
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            del(request.session['data_form'])
            return redirect('authors:login')

    return render(request, 'authors/pages/register.html', {'form': form})

def logout(requset):
    ...