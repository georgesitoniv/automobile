from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from django.http import JsonResponse, HttpResponse

from .models import Car, Color

class Index(TemplateView):
    template_name = "cars/index.html";

def get_all_colors(request):
    colors = Color.objects.all()
    context = []
    for color in colors:
        context.append({
            u"id": color.id,
            u"name": color.name,
        })
    return JsonResponse(context, safe=False)

def get_all_cars(request):
    cars = Car.objects.select_related('color')
    context = []
    for car in cars:
        context.append({
            u"id":car.id,
            u"name": car.name,
            u"color_name": car.color.name,
            u"slot_number": car.order + 1
        })
    return JsonResponse(context, safe=False)

def get_cars_by_color(request):
    id = request.GET.get('id')
    color = Color.objects.prefetch_related("cars").get(id=id)
    context = []
    for car in color.cars.all():
        context.append({
            u"id":car.id,
            u"name": car.name,
            u"color_name": car.color.name,
            u"slot_number": car.order + 1
        })
    return JsonResponse(context, safe=False)

def move_car(request):
    id = request.GET.get('id')
    direction = int(request.GET.get('direction'))
    car = Car.objects.get(id=id)
    if(direction < 0):
        car.up()
    else:
        car.down()
    return JsonResponse({}, safe=False)
