from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest


class CreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "create_auto.html")
