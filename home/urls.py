from django.urls import (
    path, )

from . import views

urlpatterns = [

    # Homepage
    path("", views.homepage, name="homepage"),

    # Authentication
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("create-account/", views.create_user, name="create-account"),
    path("delete-account/", views.delete_account, name="delete_account"),

    # Todo Routes
    path("todos/", views.show_todo, name="show_todo"),
    path("todos/create/", views.create_todo, name="create_todo"),
    path("todos/<int:todo_id>/edit/", views.edit_todo, name="edit_todo"),
    path("todos/<int:todo_id>/delete/", views.delete_todo, name="delete_todo"),
    path("todos/<int:todo_id>/toggle/", views.toggle_todo, name="toggle_todo"),
]
