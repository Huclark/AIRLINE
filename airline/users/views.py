from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    """Display information about the currently signed in user
    """
    # ensure that user is authenticated
    if not request.user.is_authenticated:
        # redirect client to login page
        return HttpResponseRedirect(reverse("login"))
    
def login_view(request):
    """This renders the login page"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # check if password matches username
        user = authenticate(request, username=username, password=password)
        if user is not None:  # it means authentication was successful
            # log the user in
            login(request, user)
            # redirect user to index route
        else: # if user authentication failed
            # render the login page again with an error message
            return render(request, "users/login.html", {
				"context": "Invalid credentials"
			})
    return render(request, "users/login.html")

def logout_view(request):
    pass
