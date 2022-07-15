import os
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_date
from portal.models import PendingPhoto, Staff, User
from .models import Blog, Message
from datetime import date
import string, random

# Create your views here.

def admin_login_required(f):
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return f(request, *args, **kwargs)
    return wrapper

@login_required
@admin_login_required
def dashboard(request):
    return render(request, 'admin-page/dashboard.html')

@login_required
@admin_login_required
def website(request):
    return render(request, 'admin-page/website.html')

@login_required
@admin_login_required
def editblogs(request):
    return render(request, 'admin-page/edit-blogs.html', {"blogs": Blog.objects.all()})

@login_required
@admin_login_required
def new_blog(request):
    if request.method == "POST":
        heading = request.POST['heading']
        desc = request.POST['desc']
        photo = request.FILES['photo']
        date = request.POST['date']
        blog = Blog(heading=heading, desc=desc, photo=photo)
        if date:
            blog.date = date
        blog.save()
    return redirect('edit_blogs')

@login_required
@admin_login_required
def update_blog(request):
    if request.method == "POST":
        id = request.POST['id']
        blog = Blog.objects.get(id=id)
        if blog:
            heading = request.POST['heading']
            desc = request.POST['desc']
            date = request.POST['date']
            try:
                photo = request.FILES['photo']
            except:
                photo = None
            blog.heading = heading
            blog.desc = desc
            blog.date = parse_date(date)
            if photo:
                os.remove(blog.photo.path)
                blog.photo = photo
            blog.save()
    return redirect('edit_blogs')

@login_required
@admin_login_required
def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    if blog:
        os.remove(blog.photo.path)
        blog.delete()
    return redirect('edit_blogs')

@login_required
@admin_login_required
def staff(request):
    return render(request, 'admin-page/staff.html', {"staff": Staff.objects.all().order_by('first_name')})

@login_required
@admin_login_required
def new_staff(request, methdods=['POST']):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        onames = request.POST['onames']
        role = request.POST['role']
        email = request.POST['email']
        gender = request.POST['gender']
        phone = request.POST['phone']
        salary = request.POST['salary']
        pwd = request.POST['password']
        date_employed = request.POST['date_employed']
        last = Staff.objects.last()
        yr = str(date.today().year)[2:]
        if last:
            num = int(last.username[-3:])
        else:
            num = 1
        rand_pwd = ''.join(random.choices(string.ascii_lowercase+string.digits, k=8))
        staff = Staff.objects.create_user(username=f'{yr}{str(num+1).zfill(3)}', password=rand_pwd if pwd == "" else pwd, email=email, gender=gender,
            first_name=fname, last_name=lname, other_names=onames, role='staff', staff_role=role.lower(), phone=phone, salary=salary, date_employed=parse_date(date_employed))
        staff.save()
    return redirect('staff')

@login_required
@admin_login_required
def update_staff(request):
    if request.method == "POST":
        uid = request.POST.get('id')
        staff = Staff.objects.filter(username=str(uid)).first()
        if staff:
            staff.first_name = request.POST.get('fname')
            staff.last_name = request.POST.get('lname')
            staff.other_names = request.POST.get('onames')
            staff.email = request.POST.get('email')
            staff.phone = request.POST.get('phone')
            staff.salary = request.POST.get('salary')
            
            role = request.POST.get('role')
            password = request.POST.get('password')
            if role != "norole":
                staff.role = role
            if password != "":
                staff.set_password(password)
            staff.save()
    return redirect('staff')

@login_required
@admin_login_required
def delete_staff(request, id):
    staff = Staff.objects.filter(username=id).first()
    if staff:
        os.remove(staff.photo.path)
        staff.delete()
    return HttpResponse()

@login_required
@admin_login_required
def classes(request):
    return render(request, 'admin-page/classes.html')

@login_required
@admin_login_required
def pupils(request):
    return render(request, 'admin-page/pupils.html')

@login_required
@admin_login_required
def messages(request):
    return render(request, 'admin-page/messages.html', {'messages':Message.objects.all().order_by('-time')})

@login_required
@admin_login_required
def pending_photos(request):
    return render(request, 'admin-page/pending-photos.html', {"pending_photos": PendingPhoto.objects.all()})

@login_required
@admin_login_required
def accept_photo(request, id):
    photo = PendingPhoto.objects.get(id=id)
    if photo:
        u = User.objects.filter(username=photo.user.username).first()
        u.photo = photo.photo
        u.save()
        photo.delete()
    return JsonResponse("ok", safe=False)

@login_required
@admin_login_required
def discard_photo(request, id):
    photo = PendingPhoto.objects.get(id=id)
    if photo:
        if len(photo.photo)>0:
            os.remove(photo.photo.path)
        photo.delete()
    return JsonResponse("ok", safe=False)
