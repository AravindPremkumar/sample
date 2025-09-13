from django.shortcuts import render,redirect
from .models import Userprofile
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        fullname = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirm')

        if password != cpassword:
            messages.error(request,'password does not match')
            return render(request,'register.html')

        if Userprofile.objects.filter(fullname=fullname).exists():
            messages.error(request,'Fullname already exist.')
            return render(request,'register.html')
        
        if Userprofile.objects.filter(email=email).exists():
            messages.error(request,'Email already exist.')
            return render(request,'register.html')

        Userprofile.objects.create(fullname=fullname,email=email,password=password)
        messages.success(request,'You have been registered succesfully!')
        return redirect('')

    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = Userprofile.objects.get(fullname=username)
        except Userprofile.DoesNotExist:
            messages.error(request, "Invalid username or password.")
            return render(request,'login.html')

        if user is not None:
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:   
            messages.error(request, "Invalid email or password.")
            return render(request,'login.html')

    return render(request, 'login.html')


def edit_profile(request, user_id):
    try:
        user = Userprofile.objects.get(id=user_id)
    except Userprofile.DoesNotExist:    
        return redirect('error_page')  # Optional: you can show a custom error

    if request.method == 'POST':
        user.fullname = request.POST.get('username')
        user.email = request.POST.get('email')
        user.bio = request.POST.get('bio')
        user.save()
        return redirect('profile', user.id)

    return render(request, 'edit_profile.html', {'user': user})



from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import HttpResponse

def home(request):
    return render(request, "lang.html")




def add(request):
    return render(request, "lang.html")









def landing(request):
    return render(request,'landing.html')