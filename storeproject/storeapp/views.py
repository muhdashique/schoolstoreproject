from django.shortcuts import render
from .models import des
# Create your views here.
def Home(request):
    obj = des.objects.all()
    return render(request,'index.html',{'result':obj})