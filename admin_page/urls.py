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

    path("edit-fees/", views.edit_fees, name="edit_fees"),
    
    path("students/", views.students, name="students"),
    path("new-student/", views.new_student, name="new_student"),
    path("update-student/", views.update_student, name="update_student"),
    path("delete-student/", views.delete_student, name="delete_student"),

    path("classes/", views.classes, name="classes"),
    path("messages/", views.get_messages, name="messages"),
    path("delete-message/<int:id>", views.delete_message, name="delete_message"),


    path("randoms/", views.randoms, name="randoms"),
    path("delete-random/<int:id>", views.delete_random, name="delete_random"),
    

    path("discard-photo/<int:id>", views.discard_photo, name="discard_photo"),
    path("pending-photos/", views.pending_photos, name="pending_photos"),
    path("accept-photo/<int:id>", views.accept_photo, name="accept_photo"),
]