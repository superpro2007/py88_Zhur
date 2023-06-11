from django.http import HttpResponse, HttpRequest
from django.views import View
from django.shortcuts import render


class HelloView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'authorization.html')