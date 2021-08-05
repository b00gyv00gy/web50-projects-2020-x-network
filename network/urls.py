
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
     
    path("save_post/<int:post_id>", views.save_post, name="save_post"),
    path("like_unlike_post/<int:post_id>", views.like_unlike_post, name="like_unlike_post"),
    path("count_likes/<int:post_id>", views.count_likes, name="count_likes")
]
