from traceback import print_tb
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Staff, Student, Test, User, PendingPhoto
from django.contrib import messages
import string, random


def staff_login_required(f):
    def wrapper(request, *args, **kwargs):
        if Staff.objects.get(username=request.user.username):
            return f(request, *args, **kwargs)
        else:
            raise Http404
    return wrapper

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('id'), password=request.POST.get('password'))
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('home')
        else:
            messages.error(request, "Incorrect ID or password")
            return redirect('login')
    return render(request, 'login.html')

@login_required
@staff_login_required
def edit_test(request, id):
    if request.method == "POST":
        form_data = request.POST
        for key in form_data:
            if key == "csrfmiddlewaretoken":
                continue
    test = Test.objects.get(id=id)
    if not test:
        raise Http404
    elif test and request.user.username != test.teacher.username:
        messages.error(request, "You are not the user that created this test")
    return render(request, "edit-test.html", {"test": test})

@login_required
@staff_login_required
def tests(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        if id:
            test = Test.objects.get(id=id)
            former = test.name
            test.name = name
            test.save()
            messages.success(f"Test renamed from {former} to {test.name} !")
        else:
            messages.error(request, f"Test \"{name}\" was not found")
    return render(request, "tests.html", {"tests":Test.objects.order_by("-id")})

@login_required
@staff_login_required
def new_test(request):
    if request.method == "POST":
        name = request.POST.get('name')
        test = Test(name=name, teacher=Staff.objects.get(username=request.user.username))
        test.save()
        code = f'{test.id}'.join(random.choices(string.ascii_lowercase+string.digits, k=5))
        test.code = code
        test.save()
        messages.success("Test created !")
    return redirect("edit_test", id=test.id)

@login_required
@staff_login_required
def delete_test(request, id):
    test = Test.objects.get(id=id)
    if test:
        n = test.name
        if request.user.username == test.teacher.username:
            test.delete()
            messages.success(request, f"Test \"{n}\" deleted")
        else:
            messages.error(request, "You are not the user that created this test so you cant delete it")
    else:
        messages.error(request, "Test not found")
    return redirect("edit_test", id=test.id)

@login_required
def profile(request, id):
    user = Staff.objects.filter(username=id).first()
    if not user:
        user = Student.objects.filter(username=id).first()
    if not user:
        raise Http404
    return render(request, 'profile.html', {"person": user})

@login_required
def home(request):
    return profile(request, request.user.username)

def upload_photo(request, id):
    user = User.objects.filter(username=id).first()
    if user:
        try:
            user.pendingphoto.delete()
        except:
            pass
        photo = PendingPhoto(photo=request.FILES.get('photo'), user=user)
        photo.save()
    return redirect('profile', id=id)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def forgot_password(request):
    return render(request, 'forgot-password.html')

def logout_user(request):
    logout(request)
    return redirect('login')
