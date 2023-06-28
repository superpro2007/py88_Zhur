from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from user.models import User

class CreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "create_user.html")

    def post(self, request: HttpRequest) -> HttpResponse:
        user_name = request.POST.get("user_name", "")
        telephone_number = request.POST.get("telephone_number", "")
        user = User(user=user_name, number=telephone_number)
        user.save()

        return render(request, "create_user.html")