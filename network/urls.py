
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_post", views.create_post, name="create_post"),
    path("profile", views.profile, name="profile"),
    path("following", views.following, name="following"),
     
    path("posts/<int:post_id>", views.save_post, name="save_post"),
    path("like_post/<int:post_id>", views.like_post, name="like_post")
]
