
from django.http import HttpResponse, HttpRequest
from django.views import View
from django.shortcuts import render


class Home(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        my_list = ['my blog', 'about me', 'donate']
        context={'articles': my_list}
        return render(request, 'home.html', context=context)
