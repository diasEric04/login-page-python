from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from main.forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# @login_required('main:user_login')
def user_logout(request):
    auth.logout(request)
    return redirect('main:index')


def user_register(request):
    form = RegisterForm()
    form_action = reverse('main:user_register')
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'conta registrada com sucesso')
            return redirect('main:user_login')
        
    context = {
        'title': 'Register',
        'form': form,
        'form_action': form_action
    }

    return render(
        request, 
        'user/register.html',
        context
    )


def user_login(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'logado com sucesso')
            return redirect('main:index')
    
    context = {
        'title': 'Login',
        'form': form
    }
    return render(
        request,
        'user/login.html',
        context
    )