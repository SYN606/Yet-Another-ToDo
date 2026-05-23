from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)

from .decorators import *
from .forms import TodoForm
from .models import CustomUser, Todo


# Homepage
def homepage(request):

    form = TodoForm()

    context = {
        "title": "Homepage",
        "form": form,
    }

    return render(
        request,
        "index.html",
        context,
    )


# Login
@check_authenticated_user  # type: ignore
def login(request):

    context = {
        "title": "Login",
    }

    if request.method == "POST":

        username = request.POST.get(
            "username",
            "",
        ).strip()

        password = request.POST.get(
            "password",
            "",
        )

        if not username or not password:

            messages.warning(
                request,
                "Please fill all required fields.",
            )

            return redirect("login", )

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user:

            auth_login(
                request,
                user,
            )

            messages.success(
                request,
                f"Welcome back, {user.username} 👋",
            )

            return redirect("homepage", )

        messages.error(
            request,
            "Invalid username or password.",
        )

        return redirect("login", )

    return render(
        request,
        "login.html",
        context,
    )


# Create Account
@check_authenticated_user  # type: ignore
def create_user(request):

    context = {
        "title": "Create Account",
    }

    if request.method == "POST":

        full_name = request.POST.get(
            "f_name",
            "",
        ).strip()

        username = request.POST.get(
            "username",
            "",
        ).strip()

        password = request.POST.get(
            "password",
            "",
        )

        if not full_name or not username or not password:

            messages.warning(
                request,
                "Please fill all required fields.",
            )

            return redirect("create-account", )

        if len(password) < 6:

            messages.error(
                request,
                "Password must contain at least 6 characters.",
            )

            return redirect("create-account", )

        if CustomUser.objects.filter(username=username, ).exists():

            messages.warning(
                request,
                "Username already taken.",
            )

            return redirect("create-account", )

        new_user = CustomUser.objects.create_user(
            username=username,
            password=password,
            full_name=full_name,
        )

        messages.success(
            request,
            "Account created successfully. Please login.",
        )

        return redirect("login", )

    return render(
        request,
        "create-account.html",
        context,
    )


# Logout
@login_required
def logout(request):

    auth_logout(request, )

    messages.info(
        request,
        "Logged out successfully.",
    )

    return redirect("homepage", )


# Create Todo
@login_required
def create_todo(request):

    if request.method != "POST":

        return redirect("homepage", )

    title = request.POST.get(
        "title",
        "",
    ).strip()

    description = request.POST.get(
        "description",
        "",
    ).strip()

    completed = request.POST.get("completed", ) == "on"

    if not title:

        messages.warning(
            request,
            "Todo title is required.",
        )

        return redirect("homepage", )

    Todo.objects.create(
        title=title,
        description=description,
        completed=completed,
        user=request.user,
    )

    messages.success(
        request,
        "Todo created successfully.",
    )

    return redirect("show_todo", )


# Show Todos
@login_required
def show_todo(request):

    todos = Todo.objects.filter(user=request.user, ).order_by("-id", )

    context = {
        "title": "Your Todos",
        "todos": todos,
    }

    return render(
        request,
        "show-todo.html",
        context,
    )


# Edit Todo
@login_required
def edit_todo(request, todo_id):

    todo = get_object_or_404(
        Todo,
        id=todo_id,
        user=request.user,
    )

    if request.method == "POST":

        title = request.POST.get(
            "title",
            "",
        ).strip()

        description = request.POST.get(
            "description",
            "",
        ).strip()

        completed = request.POST.get("completed", ) == "on"

        if not title:

            messages.warning(
                request,
                "Title cannot be empty.",
            )

            return redirect("edit_todo", todo_id=todo.id) # type: ignore

        todo.title = title
        todo.description = description
        todo.completed = completed

        todo.save()

        messages.success(
            request,
            "Todo updated successfully.",
        )

        return redirect("show_todo", )

    context = {
        "todo": todo,
        "title": "Edit Todo",
    }

    return render(
        request,
        "edit-todo.html",
        context,
    )


# Delete Todo
@login_required
def delete_todo(request, todo_id):

    todo = get_object_or_404(
        Todo,
        id=todo_id,
        user=request.user,
    )

    if request.method == "POST":

        todo.delete()

        messages.warning(
            request,
            "Todo deleted successfully.",
        )

    return redirect("show_todo", )


# Toggle Todo Status
@login_required
def toggle_todo(request, todo_id):

    todo = get_object_or_404(
        Todo,
        id=todo_id,
        user=request.user,
    )

    todo.completed = not todo.completed

    todo.save()

    status = ("completed" if todo.completed else "marked as pending")

    messages.info(
        request,
        f"Todo {status}.",
    )

    return redirect("show_todo", )


# Delete Account
@login_required
def delete_account(request):

    if request.method == "POST":

        user = request.user

        auth_logout(request, )

        user.delete()

        messages.success(
            request,
            "Your account has been deleted successfully.",
        )

        return redirect("homepage", )

    return render(
        request,
        "delete-account.html",
        {
            "title": "Delete Account",
        },
    )
