from django.shortcuts import render
from random import randint
from admin_page.models import Blog, Message, Random

# Create your views here.
def index(request):
    randoms = []
    all_randoms = list(Random.objects.all())
    for i in range(4):
        chosen = randint(1, 1000)%len(all_randoms)
        r = all_randoms[chosen]
        randoms.append(r)
        all_randoms.remove(r)
    return render(request, "index.html", {"blogs":Blog.objects.all().order_by('-date')[:4], "randoms":randoms})
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
