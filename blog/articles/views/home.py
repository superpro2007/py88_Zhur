from typing import List
from django.http import HttpResponse, HttpRequest
from django.views import View
from django.shortcuts import render
from articles.models import Article


class Home(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        articles = Article.objects.all()
        titles: List[str] = list(map(lambda article: article.title, articles))
        titles.reverse()
        
        message: str = self.request.session.get("message", '')
        context = {"articles": titles, "message": message}
        self.request.session["message"] = ""
        return render(request, "home.html", context=context)
