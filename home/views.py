from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Todo
from .decorators import *  # noqa: F403


def homepage(request):
    return render(request, "index.html", {"title": "Homepage"})


@check_authenticated_user  # noqa: F405
def login(request):
    """
    User login view
    """
    context = {"title": "Login"}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            auth_login(request, user)
            messages.success(request, "You're now logged in.")
            return redirect("homepage")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")

    return render(request, "login.html", context)


@login_required
def create_todo(request):
    """
    Create a new ToDo
    """
    if request.method == "POST":
        title = request.POST.get("title")
        todo_data = request.POST.get("todo-data")

        Todo.objects.create(title=title,
                            description=todo_data,
                            user=request.user)
        messages.success(request, "ToDo created successfully.")
        return redirect("show_todo")

    return render(request, "create-todo.html", {"title": "Create ToDo"})


@login_required
def show_todo(request):
    """
    Show all ToDos for the logged-in user
    """
    todos = Todo.objects.filter(user=request.user)
    return render(request, "show-todo.html", {
        "title": "Show all ToDos",
        "todos": todos
    })


@check_authenticated_user  # noqa: F405
def create_user(request):
    """
    Create a new user account
    """
    context = {"title": "Create Account"}
    if request.method == "POST":
        full_name = request.POST.get("f_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, "Username already taken.")
            return redirect("create-account")

        new_user = CustomUser.objects.create_user(username=username,
                                                  password=password,
                                                  full_name=full_name)
        new_user.save()

        messages.success(request,
                         "Account created successfully. Please log in.")
        return redirect("login")

    return render(request, "create-account.html", context)


@login_required
def logout(request):
    """
    Log out the current user
    """
    auth_logout(request)
    messages.warning(request, "Logged out successfully.")
    return redirect("homepage")


@login_required
def delete_account(request):
    """
    Delete the currently logged-in user's account
    """
    if request.method == "POST":
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect("homepage")

    return render(request, "delete-account.html", {"title": "Delete Account"})
