from django.http import HttpResponse, HttpRequest
from django.views import View
from django.shortcuts import render


class HelloView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'authorization.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        print(request.POST)
        return render(request, 'authorization.html')