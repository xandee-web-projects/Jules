from django.contrib import admin
from .models import PendingPhoto, Student, User, Staff

# Register your models here.
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(PendingPhoto)