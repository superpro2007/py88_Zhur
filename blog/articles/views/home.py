
from django.http import HttpResponse, HttpRequest
from django.views import View
from django.shortcuts import render
from articles.models import Article


class Home(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        articles = Article.objects.all()
        titles = list(map(lambda article: article.title, articles))
        context = {'articles': titles}
        return render(request, 'home.html', context=context)

