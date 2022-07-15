from django.shortcuts import render
from pkg_resources import require

from admin_page.models import Blog, Message

# Create your views here.
def index(request):
    return render(request, "index.html", {"blogs":Blog.objects.all().order_by('-date')[:4]})
def about(request):
    return render(request, "about.html")
def blog(request):
    return render(request, "blog.html", {"blogs":Blog.objects.all().order_by('-date')})
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        contact = request.POST['contact']
        sub = request.POST['subject']
        msg = request.POST['msg']
        Message(name=name, contact=contact, subject=sub, message=msg).save()
    return render(request, "contact.html")
def fees(request):
    return render(request, "fees.html")
