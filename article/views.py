from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import os
from django.conf import settings
from django.conf.urls.static import static
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .models import Article, Category, Author
from .forms import ArticleForm

def detailView(request, slugInput):
    articles            = Article.objects.all()
    articles_detail     = Article.objects.get(slug=slugInput)
    articles_by_comment = Article.objects.order_by('comment_count')[0:3]
    categories          = Category.objects.all()
    context             = {
        'page_title'            :'Cryppy | '+ articles_detail.title,
        'articles'              :articles,
        'articles_by_comment'   :articles_by_comment,
        'categories'            :categories,
        'articles_detail'       :articles_detail,
    }
    return render(request, 'article/detail.html', context)

def categoryView(request, categoryInput):
    articles            = Article.objects.all()
    articles_detail     = Article.objects.filter(categories__title=categoryInput)
    articles_by_comment = Article.objects.order_by('comment_count')[0:3]
    cat_page            = Category.objects.filter(title=categoryInput)
    categories          = Category.objects.all()
    latest              = Article.objects.order_by('-timestamp')
    page                = request.GET.get('page',1)
    paginator           = Paginator(articles_detail,2)
    try:
        articles_page = paginator.page(page)
    except PageNotAnInteger:
        articles_page = paginator.page(1)
    except EmptyPage:
        articles_page = paginator.page(paginator.num_pages)
    context             = {
        'page_title'            :"Cryppy | Articles by Category",
        'articles'              :articles,
        'articles_by_comment'   :articles_by_comment,
        'categories'            :categories,
        'latest'                :latest,
        'cat_page'              :cat_page,
        'articles_page'         :articles_page,
    }
    return render(request, 'article/category.html', context)

@login_required
def createView(request):
    author_request     = Author.objects.filter(user__username=request.user)
    post_form          = ArticleForm(request.POST or None, request.FILES or None, initial={'author': request.user})
    if request.method == 'POST':
        if post_form.is_valid():
            post_item = post_form.save()
            post_item.save()
            messages.success(request,'Succesfully, new article has been created!')
            return redirect('accounts:dashboard')
        else:
            messages.error(request,'Error! You should check in on some of those fields below.')
            return redirect('accounts:createArticle')
    context = {
        'page_title'    :'Cryppy | Create Article',
        'heading'       :'Form | Create Article',
        'post_form'     :post_form,
        'author'        :author_request,
    }
    
    return render(request, 'accounts/create.html', context)

@login_required
def editView(request, update_id):
    author_request = Author.objects.filter(user__username=request.user)
    post_update = Article.objects.get(id=update_id)
    data = {
		'title'		    : post_update.title,
		'overview'		: post_update.overview,
		'content'		: post_update.content,
		'author'		: post_update.author,
        'thumbnail'     : post_update.thumbnail,
	}
    post_form = ArticleForm(
        request.POST or None, 
        request.FILES or None, 
        initial=data, 
        instance=post_update,
    )
    if request.method == 'POST':
        if post_form.is_valid():
            # os.replace(os.path.join(settings.MEDIA_ROOT, post_update.thumbnail.name, post_update.thumbnail.name+'edit'))
            post_item = post_form.save()
            post_item.save()
            # post_item.save()
            messages.success(request,'Succesfully, article has been changed!')
            return redirect('accounts:dashboard')
        else:
            messages.error(request,'Error! You should check in on some of those fields below.')
            return redirect('accounts:createArticle')
    context = {
        'page_title'    :'Cryppy | Edit Article',
        'heading'       :'Form | Edit Article',
        'post_form'     :post_form,
        'author'        :author_request,
    }
    return render(request, 'accounts/create.html', context)

@login_required
def deleteView(request, delete_id):
    files = Article.objects.filter(id=delete_id)
    for picture in files:
        if picture.thumbnail:
            os.remove(os.path.join(settings.MEDIA_ROOT, picture.thumbnail.name))
            Article.objects.filter(id=delete_id).delete()
            messages.success(request,'Succesfully, article has been deleted!')
            return redirect('accounts:dashboard')
        else:
            Article.objects.filter(id=delete_id).delete()
            messages.success(request,'Succesfully, article has been deleted!')
            return redirect('accounts:dashboard')

def deleteConfirmArticleView(request, delete_id):
    total_articles  = Article.objects.get(id=delete_id)
    context = {
        'page_title':'Cryppy | Dashboard User',
        'heading_1': 'Welcome to Dashboard',
        'total_articles':total_articles,
    }
    return render(request, "accounts/delete_confirm_article.html", context)