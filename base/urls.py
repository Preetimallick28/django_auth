from django.urls import path
from base import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('bookings/',views.bookings,name='bookings'),
    path('history/',views.history,name='history'),
]
