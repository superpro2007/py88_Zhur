from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from articles.models import Article
class CreateArticle(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'create_article.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        title = request.POST.get('title')
        text = request.POST.get('text')
        article = Article(title=title, text=text)
        article.save()
        return redirect('home')
