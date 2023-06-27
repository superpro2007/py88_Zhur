from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest


class CreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "create_auto.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        car_brand = request.POST.get("car_brand", "")
        car_model = request.POST.get("car_model", "")
        vin = request.POST.get("vin", "")
        print(f"{car_brand}, {car_model}, {vin}")

        return render(request, "create_auto.html")
