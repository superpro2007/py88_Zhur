from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from customer.models import Customer

class CreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "create_customer.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        customer_name = request.POST.get("customer_name", "")
        telephone_number = request.POST.get("telephone_number", "")
        customer = Customer(name=customer_name, number=telephone_number)
        customer.save()

        return render(request, "create_customer.html")