from datetime import date
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Staff, Student, User, PendingPhoto
from django.utils.dateparse import parse_date

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['id'], password=request.POST['password'])
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            return redirect('dashboard')
        else:
            return HttpResponse("Incorrect")
    return render(request, 'login.html')


# @login_required('login')
def profile(request, id):
    user = Staff.objects.filter(username=id).first()
    if not user:
        user = Student.objects.filter(username=id).first()
    if not user:
        return HttpResponse("404 not found")
    template = "admin-page/base.html" if request.user.is_superuser else "bases/base_"+request.user.role+".html"
    return render(request, 'profile.html', {"person": user, "template":template })

def upload_photo(request, id):
    user = User.objects.filter(username=id).first()
    if user:
        photo = PendingPhoto(photo=request.FILES['photo'], user=user)
        photo.save()
    return redirect('profile', id=id)

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)