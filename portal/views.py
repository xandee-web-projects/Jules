from datetime import date
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Staff, Student, User, PendingPhoto
from django.utils.dateparse import parse_date
from django.contrib import messages
from django.conf import settings

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['id'], password=request.POST['password'])
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('profile', id=user.username)
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
        return HttpResponse("404 not found")
    return render(request, 'profile.html', {"person": user})

def upload_photo(request, id):
    user = User.objects.filter(username=id).first()
    if user:
        photo = PendingPhoto(photo=request.FILES['photo'], user=user)
        photo.save()
    return redirect('profile', id=id)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def logout(request):
    logout(request)
    redirect('login')