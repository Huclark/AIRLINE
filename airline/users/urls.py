from django.urls import path

from . import views

urlpatterns = [
    # displays information about the currently signed in user
    path("", views.index, name="index"),
    # displays the login page for user to login
    path("login", views.login_view, name="login"),
    # allows users to logout
    path("logout", views.logout_view, name="logout")
]
