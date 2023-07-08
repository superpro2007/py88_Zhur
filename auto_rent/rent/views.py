from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from auto.models import Car
from customer.models import Customer
from rent.models import Rent


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        rents = Rent.objects.all()
        rents_for_page = []
        for rent in rents:
            rents_for_page.append(
                {
                    "brand": rent.car.brand,
                    "model": rent.car.model,
                    "name": rent.customer.name,
                }
            )

        return render(request, "index.html", context={"rents": rents_for_page})


class CreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "create_rent.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        phone_number = request.POST.get("telephone_number", "")
        vin = request.POST.get("vin", "")
        # one_entry = Entry.objects.get(pk=1)
        car = Car.objects.get(vin=vin)
        customer = Customer.objects.get(number=phone_number)
        rent = Rent(car=car, customer=customer)
        rent.save()
        return render(request, "create_rent.html")
