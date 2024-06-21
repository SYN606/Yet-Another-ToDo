from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth  # type: ignore
from .decorators import *  # noqa: F403
from django.contrib.auth import logout as auth_logout
from .models import Todo

def homepage(request):
    data = {"title": "Homepage"}
    return render(request, "index.html", data)


@check_authenticated_user  # noqa: F405
def login(request):
    data = {"title": "Login"}
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)

            messages.success(request, "You're now logged in.")
            return redirect("homepage")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
    else:
        return render(request, "login.html", data)


def create_todo(request):
    if request.method == "POST":
        title = request.POST["title"]
        todo_data = request.POST["todo-data"]

        new_todo = Todo(
            title=title,
            description=todo_data,
            user = request.user
        )

        new_todo.save()
        return redirect("homepage")

def show_todo(request):
    todo = Todo.objects.filter(user = request.user)

    data = {
        "title": "Show all Todo",
        "todos" : todo 
    }
    return render(request, 'show-todo.html', data)


@check_authenticated_user  # noqa: F405
def create_user(request):
    data = {
        "title": "Create User Account"
    }
    if request.method == "POST":
        full_name = request.POST["f_name"]
        username = request.POST["username"]
        password = request.POST["password"]

        new_user = User.objects.create_user(full_name, username, password)  # type: ignore
        new_user.save()

        messages.success(request, "Your account has been created successfully.")
        return redirect("login")

    else:
        return render(request, "create-account.html", data)


def logout(request):
    auth_logout(request)
    messages.warning(request, 'Logged out successfully')
    return redirect('homepage')


def delete(request):
    pass
