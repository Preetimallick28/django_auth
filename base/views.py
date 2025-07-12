from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def bookings(request):
    return render(request,'bookings.html')
def history(request):
    return render(request,'history.html')

# sorry sir