from django.shortcuts import render

# Create your views here.
def home(request):
    return render('','home.html')
def about(request):
    return render('about/','about.html')
def bookings(request):
    return render('bookings/','bookings.html')
def history(request):
    return render('history/','history.html')
