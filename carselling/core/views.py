from django.shortcuts import render,redirect
from django.http import HttpResponse
from cars.models import Category,Car
from .forms import Signup
# Create your views here.

def index(request):
    cars = Car.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request,'core/index.html',{
        'categories':categories,
        'cars':cars,
    })

def about(request):
    return render(request, 'core/about.html')

def commu(request):
    return render(request, 'core/commu.html')

def signup(request):
    if request.method=='POST':
        form = Signup(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = Signup()
    return render(request, 'core/signup.html',{
        'form':form
    })

    