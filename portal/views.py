from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Staff, Student, User, PendingPhoto
from django.contrib import messages

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['id'], password=request.POST['password'])
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
        photo = PendingPhoto(photo=request.FILES['photo'], user=user)
        photo.save()
    return redirect('profile', id=id)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def logout_user(request):
    logout(request)
    return redirect('login')
