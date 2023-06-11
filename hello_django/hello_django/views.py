from django.http import HttpResponse, HttpRequest
from django.views import View


class HelloView(View):
    def get(self, request: HttpRequest):
        return HttpResponse('Hello world')