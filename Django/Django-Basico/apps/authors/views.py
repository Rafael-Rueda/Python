from django.shortcuts import render, redirect
from django.contrib.auth import logout as user_logout
from django.contrib.auth import login as user_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from apps.authors.forms import RegisterForm, LoginForm, ProfileForm

@login_required
def logout(request):
    if request.method == 'POST':
        user_logout(request)
    return redirect('home:home')

def login(request):
    if 'data-login' in request.session:
        form = LoginForm(request.session.get('data-login'))
        del(request.session['data-login'])
    else:
        form = LoginForm()

    if request.method == 'GET':
        return render(request, 'authors/pages/login.html', context={'form': form})
    elif request.method == 'POST':

        request.session['data-login'] = request.POST
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])

            if user is not None:
                user_login(request, user)
                
                del(request.session['data-login'])
                return redirect('home:home')
            else:
                return redirect('authors:login')

def register(request):
    if 'data-form' in request.session:
        form = RegisterForm(request.session.get('data-form'))
        del(request.session['data-form'])
    else:
        form = RegisterForm()
    
    if request.method == 'GET':
        return render(request, 'authors/pages/register.html', context={'form': form})
    elif request.method == 'POST':

        request.session['data-form'] = request.POST
        modelform = RegisterForm(request.POST)

        if modelform.is_valid():
            user = modelform.save(commit=False)
            password = modelform.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            del(request.session['data-form'])

            userlogin = authenticate(request, username=modelform.cleaned_data['username'], password=modelform.cleaned_data['password'])
            if userlogin != None:
                user_login(request, userlogin)

            return redirect('home:home')
        return redirect('authors:register')
    
def profile(request):
    form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return render(request, 'authors/pages/profile.html', {'form': form})
    return render(request, 'authors/pages/profile.html', {'form': form})