from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="admin_dashboard"),
    path("website/", views.website, name="website"),

    path("edit-blogs/", views.editblogs, name="edit_blogs"),
    path("new-blog/", views.new_blog, name="new_blog"),
    path("update-blog/", views.update_blog, name="update_blog"),
    path("delete-blog/<int:id>", views.delete_blog, name="delete_blog"),

    path("staff/", views.staff, name="staff"),
    path("new-staff/", views.new_staff, name="new_staff"),
    path("update-staff/", views.update_staff, name="update_staff"),
    path("delete-staff/<str:id>", views.delete_staff, name="delete_staff"),


    path("classes/", views.classes, name="classes"),
    path("pupils/", views.pupils, name="pupils"),

    path("discard-photo/<int:id>", views.discard_photo, name="discard_photo"),
    path("pending-photos/", views.pending_photos, name="pending_photos"),
    path("accept-photo/<int:id>", views.accept_photo, name="accept_photo"),
]