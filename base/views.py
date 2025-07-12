from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required - this is a decorator which will not allowed user to access with login or user verification
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
@login_required
def about(request):
    return render(request,'about.html')
@login_required
def bookings(request):
    return render(request,'bookings.html')
@login_required
def history(request):
    return render(request,'history.html')

# sorry sir