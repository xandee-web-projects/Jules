from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("profile/<str:id>", views.profile, name="profile"),
    path("upload-photo/<int:id>", views.upload_photo, name="upload_photo"),
]