from django.contrib import messages, auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        # Get form value
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            # Check Username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'This Email is being used')
                    return redirect('register')
                else:
                    # Looks Good
                                  # # Login After Register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')     
                        user = User.objects.create_user(
                            username=username, first_name=first_name, last_name=last_name, password=password, email=email)
    
                        user.save()
                        messages.success(
                            request, 'You are now registered and Noe you can Login')
                        return redirect('login')
        else:
            messages.error(request, 'Pasword Do Not Match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in ')
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('/')

