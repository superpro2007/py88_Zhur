from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "index.html")
    
class CreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "create_rent.html")