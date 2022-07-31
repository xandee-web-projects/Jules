from django.contrib import admin
from .models import ClassFees, PendingPhoto, Student, User, Staff, Class, Test, Question, Option

# Register your models here.
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(User)
admin.site.register(PendingPhoto)
admin.site.register(ClassFees)
admin.site.register(Class)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Option)