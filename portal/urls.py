from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.home, name="home"),
    path("edit-test/<int:id>", views.edit_test, name="edit_test"),
    path("new-test/", views.new_test, name="new_test"),
    path("delete-test/<int:id>", views.delete_test, name="delete_test"),    
    path("tests/", views.tests, name="tests"),
    path("forgot_password/", views.forgot_password, name="forgot_password"),
    path("profile/<str:id>", views.profile, name="profile"),
    path("upload-photo/<int:id>", views.upload_photo, name="upload_photo"),
]