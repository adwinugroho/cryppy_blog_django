from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from article.models import Article, Category, Author

def indexView(request):
    all_articles    = Article.objects.all()
    author_blog     = Author.objects.filter(id=1)
    articles        = Article.objects.order_by('comment_count')[0:3]
    categories      = Category.objects.all()
    latest          = Article.objects.order_by('-timestamp')
    page            = request.GET.get('page',1)
    paginator       = Paginator(latest,4)
    try:
        articles_page = paginator.page(page)
    except PageNotAnInteger:
        articles_page = paginator.page(1)
    except EmptyPage:
        articles_page = paginator.page(paginator.num_pages)
    context = {
        'page_title':"Cryppy | Built on Mission",
        'heading_1':'Latest Post',
        'articles':articles,
        'author_blog':author_blog,
        'all_articles':all_articles,
        'categories':categories,
        'latest':latest,
        'articles_page':articles_page,
    }
    return render(request, 'index.html', context)

def aboutView(request):
    articles            = Article.objects.all()
    articles_by_comment = Article.objects.order_by('comment_count')[0:3]
    categories          = Category.objects.all()
    latest              = Article.objects.order_by('-timestamp')
    context             = {
        'page_title': 'Cryppy | About Me',
        'heading': 'How is the world now?',
        'articles':articles,
        'categories':categories,
        'latest':latest,
        'articles_by_comment':articles_by_comment,
    }
    return render(request, 'article/about.html', context)