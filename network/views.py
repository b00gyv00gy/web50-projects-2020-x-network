from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from django.core import serializers

from .models import User, Post, Like, Follower

class ContentForm(forms.Form):
    pass

def index(request):
    
    posts = Post.objects.all().order_by('-created')

    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "network/index.html",{
        "page_obj": page_obj
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

    posts = Post.objects.filter(author=request.user).order_by('-created')
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/profile.html", {
        "follows": Follower.objects.filter(follows=request.user).count(),
        "followed": Follower.objects.filter(followed=request.user).count(),
        "page_obj": page_obj
    })

@login_required
def following(request):

    follows = Follower.objects.filter(follows=request.user)
    followed = []
    for user in follows:
        followed.append(user.followed)
    posts = Post.objects.filter(author__in=followed).order_by('-created')

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, "network/index.html", {
        "page_obj": page_obj
    })

@csrf_exempt
@login_required
def save_post(request, post_id):

    try:
        post = Post.objects.get(author=request.user, pk=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get("content") is not None:
            post.content = data["content"]
        post.save()
        return HttpResponse(status=204)

    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)

@csrf_exempt
@login_required
def like_unlike_post(request, post_id):

    post = Post.objects.get(pk=post_id)
    user = request.user

    if Like.objects.filter(post=post, user=user).count() > 0:
        Like.objects.filter(post=post, user=user).delete()
        return HttpResponse(status=200)

    else:    
        try:
            like = Like(post=post, user=user)
            like.save()
            return HttpResponse(status=204)
        except IntegrityError as e:
            print(e)
            return JsonResponse({
                "error": "could not procees like"
            })

def count_likes(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = request.user
    like_status = Like.objects.filter(post=post, user=user).count() > 0

    num_of_likes = Like.objects.filter(post=post).count()

    return JsonResponse({
        "num_of_likes": num_of_likes,
        "like_status": like_status
    })




