from django.shortcuts import render
from django.http import HttpResponse
from cars.models import Category,Car
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

    