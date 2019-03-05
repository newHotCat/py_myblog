from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

# Create your views here.


def index(request):
    article = Article.objects.all()
    return render(request, 'blog/index.html', {'article': article})


def article_page(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
