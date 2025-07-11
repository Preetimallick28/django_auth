from django.shortcuts import render , redirect
from django.contrib.auth.models import User
# from django.contrib import messages
# we are learning django session base authentication system
# Create your views here.
def login_view(request):
    return render(request,'login.html')

def register_view(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        print(firstname,lastname,email,username)
        # if User.objects.filter(username=username).exists():
        #     messages.error(request, 'Username already taken.')
        #     return redirect('register')
        u=User.objects.create(
            first_name = firstname,
            last_name = lastname,
            email = email,
            username = username,
        )
        # set_password() used to store password in encrypted format
        u.set_password(password)
        u.save()
        return redirect('login')
    #IntegrityError - unique constraint failed:auth_username -  when same username is used
        
    return render(request,'register.html')