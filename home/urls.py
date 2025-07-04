from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("create-account/", views.create_user, name="create-account"),
    path("create-todo/", views.create_todo, name="create_todo"),
    path("show-todo/", views.show_todo, name="show_todo"),
    path("delete-account/", views.delete_account, name="delete_account"),

    # Extra routes
    path("todo/<int:todo_id>/edit/", views.edit_todo, name="edit_todo"),
    path("todo/<int:todo_id>/delete/", views.delete_todo, name="delete_todo"),
    path("todo/<int:todo_id>/toggle/", views.toggle_todo, name="toggle_todo"),
]
