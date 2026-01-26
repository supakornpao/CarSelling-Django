from django.shortcuts import render,get_object_or_404
from .models import Car
# Create your views here.
def detail(request,pk):
    car = get_object_or_404(Car,pk=pk)
    related_cars=Car.objects.filter(category=car.category,is_sold=False).exclude(pk=pk)[0:3]

    return render(request,'cars/detail.html',{
        'car':car,
        'related_car':related_cars
    })