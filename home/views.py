from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Todo
from .decorators import *
from .forms import TodoForm


def homepage(request):
    form = TodoForm()
    context = {"title": "Homepage", "form": form}
    return render(request, "index.html", context)


@check_authenticated_user  # type: ignore
def login(request):
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


@check_authenticated_user  # type: ignore
def create_user(request):
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
    auth_logout(request)
    messages.warning(request, "Logged out successfully.")
    return redirect("homepage")


@login_required
def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        todo_data = request.POST.get("todo-data")

        Todo.objects.create(title=title,
                            description=todo_data,
                            user=request.user)
        messages.success(request, "ToDo created successfully.")
        return redirect("show_todo")

    return render(request, "show-todo.html", {"title": "Create ToDo"})


@login_required
def show_todo(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, "show-todo.html", {
        "title": "Show all ToDos",
        "todos": todos
    })


@login_required
def edit_todo(request, todo_id):
    """
    Edit an existing ToDo
    """
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)

    if request.method == "POST":
        todo.title = request.POST.get("title")
        todo.description = request.POST.get("todo-data")
        todo.save()
        messages.success(request, "ToDo updated successfully.")
        return redirect("show_todo")

    return render(request, "edit-todo.html", {
        "todo": todo,
        "title": "Edit ToDo"
    })


@login_required
def delete_todo(request, todo_id):
    """
    Delete a ToDo
    """
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    messages.warning(request, "ToDo deleted successfully.")
    return redirect("show_todo")


@login_required
def toggle_todo(request, todo_id):
    """
    Toggle completed/incomplete status
    """
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    status = "completed" if todo.completed else "marked as incomplete"
    messages.info(request, f"ToDo {status}.")
    return redirect("show_todo")


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
