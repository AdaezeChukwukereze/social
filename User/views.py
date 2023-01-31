from django.shortcuts import render, redirect
from .form import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome to 5b7, {username}")
            return redirect("/")   #after saving the form redirect the person to homepage

    else:
        form = UserRegisterForm()
    return render(request, "User/register.html", {"form": form})


def home_page(request):
    return render(request, "User/home.html")
