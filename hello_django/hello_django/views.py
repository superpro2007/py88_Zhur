from django.http import HttpResponse, HttpRequest
from django.views import View
from django.shortcuts import render


class HelloView(View):
    def get(self, request: HttpRequest):
        color = {
            'color': 'red',
            'text': 'hello!'
        }
        return render(request, 'hello.html', context=color)


class HelloWorldView(View):
    def get(self, request: HttpRequest):
        color = {
            'color': 'blue',
            'text': 'hello world!'
        }
        return render(request, 'hello.html', context=color)