
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_post", views.create_post, name="create_post"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("following", views.following, name="following"),
    path("follow/<str:username>", views.follow, name="follow"), 
    path("follow_status/<str:username>", views.follow_status, name="follow_status"),
    path("save_post/<int:post_id>", views.save_post, name="save_post"),
    path("like_unlike_post/<int:post_id>", views.like_unlike_post, name="like_unlike_post"),
    path("count_likes/<int:post_id>", views.count_likes, name="count_likes")
]
