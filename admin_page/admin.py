from django.contrib import admin
from .models import Blog, Message, Random

# Register your models here.
admin.site.register(Blog)
admin.site.register(Message)
admin.site.register(Random)
