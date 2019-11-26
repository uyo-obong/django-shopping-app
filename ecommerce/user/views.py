from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from ecommerce.core.models import Category
from .forms import RegisterForm, ContactForm


def contact_us(request):
    form = ContactForm()
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # raise Exception(form)
            form.save()
            return redirect('home.core')
        else:
            form = ContactForm()

    context = {
        "form": form,
        "categories": categories
    }
    return render(request, "users/contact.html", context)


def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            # Cleaned(normalized) data
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']

            #  Use set_password here
            user.set_password(password)
            user.save()

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home.core')
    else:
        form = RegisterForm()

    context = {
        "form": form
    }
    return render(request, 'users/register.html', context)


def login_user(request):
    form = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            form['user'] = request.user
            return redirect('home.core')
        else:
            form['error'] = 'Provide Valid Credentials'
            return render(request, "users/login.html", form)
    else:
        return render(request, "users/login.html", form)


def user_logout(request):
    logout(request)
    return redirect('login.user')
