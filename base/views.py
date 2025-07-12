from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
# @login_required - this is a decorator which will not allowed user to access with login or user verification

# assignement
# create new flight and task with authentication system
# old password and new password
# handle integrity error




@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated: #it will return true and if false template will not rendered
        return render(request,'home.html')

@login_required
def about(request):
    if request.user.is_authenticated:
        return render(request,'about.html')

@login_required
def bookings(request):
    if request.user.is_authenticated:
        return render(request,'bookings.html')

@login_required
def history(request):
    if request.user.is_authenticated:
        return render(request,'history.html')

