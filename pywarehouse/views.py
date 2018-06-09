from django.shortcuts import render
from django.http import HttpResponse

from .models import Article

# Create your views here.


def home(request):
    return HttpResponse("Under Construction.")


def start(request):
    return render(request, 'start.html', {'start': start})


def article_overview(request):
    articles = Article.objects.all()
    return render(request, 'article_overview.html',
                  {'article_overview': article_overview})
