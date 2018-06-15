from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewArticleForm
from .models import Article

# Create your views here.


def home(request):
    return HttpResponse("Under Construction.")


def start(request):
    return render(request, 'start.html', {'start': start})


def article_overview(request):
    articles = Article.objects.all()
    return render(request, 'article_overview.html',
                  {'articles': articles})


def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detailed.html', {'article': article})


def new_article(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST)
        if form.is_valid():

            # Saving the input
            new_article = form.save()

            # redirect to the created article by using the article_view method.
            # return redirect('article_view', pk=article_number)
    else:
        form = NewArticleForm()
    return render(request, 'new_article.html', {'form': form})
