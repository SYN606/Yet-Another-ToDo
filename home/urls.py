from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("create-account", views.create_user, name="create-account"),
    path('create_todo', views.create_todo, name="create_todo"), # type: ignore
    path('show_todo', views.show_todo, name="show_todo")

]
