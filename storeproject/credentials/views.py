from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,"confirm.html")
        else:
            messages.info(request, 'invalid credential')
            return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('register')

            user = User.objects.create_user(username=username,  password=password)


            user.save();
            return redirect("login")

            print("user created")
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def form(request):


    return render(request,"form.html")

def home(request):
    return redirect('/')


def msg(request):
    return render(request, "msg.html")


from django.shortcuts import render


