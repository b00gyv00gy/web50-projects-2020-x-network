from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms

from .models import User, Post, Like, Follower

class ContentForm(forms.Form):
    pass

def index(request):
    return render(request, "network/index.html",{
        "posts": Post.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def create_post(request):

    form = ContentForm(request.POST)

    if request.method == "POST":
        content = request.POST["content"]
        author = request.user
        
        try:
            post = Post(content=content, author=author)
            post.save()
            
        except IntegrityError:
            return render(request, "network/index.html", {
                "message": "smth is wrong"
            })
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/index.html")

def profile(request):
    return render(request, "network/profile.html", {
        "follows": Follower.objects.filter(follows=request.user).count(),
        "followed": Follower.objects.filter(followed=request.user).count(),
        "posts": Post.objects.filter(author=request.user)
    })

def following(request):

    follows = Follower.objects.filter(follows=request.user)
    return render(request, "network/index.html", {
        "posts": Post.objects.filter(author__in=follows)
    })

