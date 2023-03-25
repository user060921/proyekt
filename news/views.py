from django.shortcuts import render, get_object_or_404
from .models import Article
from django.core.paginator import Paginator

def home(request):
    data= Article.objects.all()
    p = Paginator(data, 2)
    page = request.GET.get('page')
    context = {
        'data': p.get_page(page)
    }
    return render(request, 'index.html',context)



def article_detail(request, slug):
    data = get_object_or_404(Article, slug=slug)
    context = {
        'data': data
    }
    return render(request, 'index.html', context)


