from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from auto.models import Car

class CreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "create_auto.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        car_brand = request.POST.get("car_brand", "")
        car_model = request.POST.get("car_model", "")
        vin = request.POST.get("vin", "")
        car = Car(brand=car_brand, model=car_model, vin=vin)
        car.save()

        return render(request, "create_auto.html")
