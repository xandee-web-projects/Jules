from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.home, name="home"),
    path("profile/<str:id>", views.profile, name="profile"),
    path("upload-photo/<int:id>", views.upload_photo, name="upload_photo"),
]