from django.shortcuts import render, redirect
from .forms import SignUpForm, EditProfileForm, EditPasswordForm
from article.forms import CategoryForm, AuthorForm
from django.contrib.auth import login, authenticate, logout, get_user_model, update_session_auth_hash
from article.models import Article, Author, Category
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def registerView(request):
    form    = SignUpForm(request.POST or None)
    context = {
        'form':form,
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get('password1')
            messages.success(request,'Succesfully, account has been created!')
            return redirect('accounts:login')
        else:
            form = SignUpForm()
    return render(request, 'accounts/register.html', context)


@login_required()
def dashboardView(request):
    total_author    = Author.objects.all()
    total_article   = Article.objects.all()
    author_request  = Author.objects.filter(user__username=request.user)
    article         = Article.objects.filter(author__user__username=request.user)
    context         = {
        'page_title':'Cryppy | Dashboard User',
        'heading_1':'Welcome to Dashboard',
        'article':article,
        'author':author_request,
        'total_author':total_author,
        'total_article':total_article,
    }
    return render(request, 'accounts/index.html', context)

def editProfileView(request):
    author_request = Author.objects.filter(user__username=request.user)
    post_update = Author.objects.get(user__username=request.user)
    data        = {
        'email'         :post_update.user.email,
        'first_name'    :post_update.user.first_name,
        'last_name'     :post_update.user.last_name,
        'password'      :post_update.user.password,
    }
    post_form = EditProfileForm(
        request.POST or None,
        initial=data,  
        instance=request.user,
    )
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()
            messages.success(request,'Succesfully, profile has been changed!')
            return redirect('accounts:dashboard')
        else:
            messages.error(request,'Error! You should check on some of those fields below.')
            return redirect('accounts:profile')
    else:
        context = {
            'page_title'    :'Cryppy | Edit Profile',
            'heading'       :'Form | Edit Profile',
            'post_form'     :post_form,
            'author'        :author_request,
        }
    return render(request, 'accounts/create.html', context)

def changePasswordView(request):
    author_request = Author.objects.filter(user__username=request.user)
    post_form = EditPasswordForm(request.user, request.POST)
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()
            update_session_auth_hash(request, post_form.user)
            messages.success(request,'Succesfully, profile has been changed!')
            return redirect('accounts:dashboard')
        else:
            messages.error(request,'Error! You should check on some of those fields below.')
            return redirect('accounts:change-password')
    else:
        context = {
            'page_title'    :'Cryppy | Edit Profile',
            'heading'       :'Form | Edit Profile',
            'post_form'     :post_form,
            'author'        :author_request,
        }
    return render(request, 'accounts/change_password.html', context)

@login_required()
def listCategoryandAuthorView(request):
    total_category  = Category.objects.all()
    total_author    = Author.objects.exclude(user__username='admin')
    context = {
        'page_title':'Cryppy | Dashboard User',
        'heading_1': 'Welcome to Dashboard',
        'total_category':total_category,
        'total_author':total_author,
    }
    return render(request, 'accounts/list.html', context)

@login_required()
def createCategoryView(request):
    author_request     = Author.objects.filter(user__username=request.user)
    post_form          = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if post_form.is_valid():
            post_item = post_form.save()
            post_item.save()
            messages.success(request,'Succesfully, new category has been created!')
            return redirect('accounts:listCategoryandAuthor')
        else:
            messages.error(request,'Error! You should check on some of those fields below.')
            return redirect('accounts:createCategory')
    context = {
        'page_title'    :'Cryppy | Create Category',
        'heading'       :'Form | Create Category',
        'post_form'     :post_form,
        'author'        :author_request,
    }
    return render(request, 'accounts/create_staff.html', context)

@login_required()
def createAuthorView(request):
    author_request     = Author.objects.filter(user__username=request.user)
    post_form          = AuthorForm(request.POST or None)
    if request.method == 'POST':
        if post_form.is_valid():
            post_item = post_form.save()
            post_item.save()
            messages.success(request,'Succesfully, new author has been created!')
            return redirect('accounts:listCategoryandAuthor')
        else:
            messages.error(request,'Error! You should check on list author.')
            return redirect('accounts:createAuthor')
    context = {
        'page_title'    :'Cryppy | Create Author',
        'heading'       :'Form | Create Author',
        'post_form'     :post_form,
        'author'        :author_request,
    }
    return render(request, 'accounts/create_staff.html', context)

@login_required()
def editCategoryView(request, update_id):
    author_request = Author.objects.filter(user__username=request.user)
    post_update = Category.objects.get(id=update_id)
    data = {
		'title'		    : post_update.title,
	}
    post_form = CategoryForm(
        request.POST or None,  
        initial=data, 
        instance=post_update,
    )
    if request.method == 'POST':
        if post_form.is_valid():
            post_item = post_form.save()
            post_item.save()
            messages.success(request,'Succesfully, category has been changed!')
            return redirect('accounts:listCategoryandAuthor')
        else:
            messages.error(request,'Error! You should check on some of those fields below.')
            return redirect('accounts:createCategory')
    else:
        context = {
            'page_title'    :'Cryppy | Edit Category',
            'heading'       :'Form | Edit Category',
            'post_form'     :post_form,
            'author'        :author_request,
        }
        return render(request, 'accounts/create_staff.html', context)

@login_required
def deleteConfirmCategoryView(request, delete_id):
    total_category  = Category.objects.get(id=delete_id)
    context = {
        'page_title':'Cryppy | Dashboard User',
        'heading_1': 'Welcome to Dashboard',
        'total_category':total_category,
    }
    return render(request, "accounts/delete_confirm_category.html", context)

@login_required
def deleteConfirmAuthorView(request, delete_id):
    total_author  = Author.objects.get(id=delete_id)
    context = {
        'page_title':'Cryppy | Dashboard User',
        'heading_1': 'Welcome to Dashboard',
        'total_author':total_author,
    }
    return render(request, "accounts/delete_confirm_author.html", context)

@login_required()
def deleteCategoryView(request, delete_id):
    Category.objects.filter(id=delete_id).delete()
    messages.success(request,'Succesfully, category has been deleted!')
    return redirect('accounts:listCategoryandAuthor')

@login_required()
def editAuthorView(request, update_id):
    author_request = Author.objects.filter(user__username=request.user)
    post_update = Author.objects.get(user__id=update_id)
    get_user = User.objects.get(id=update_id)
    data        = {
        'email'         :post_update.user.email,
        'first_name'    :post_update.user.first_name,
        'last_name'     :post_update.user.last_name,
        'password'      :post_update.user.password,
    }
    post_form = EditProfileForm(
        request.POST or None,
        initial=data,  
        instance=get_user,
    )
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()
            messages.success(request,'Succesfully, author has been changed!')
            return redirect('accounts:listCategoryandAuthor')
        else:
            messages.error(request,'Error! You should check on some of those fields below.')
            return redirect('accounts:createAuthor')
    else:
        context = {
            'page_title'    :'Cryppy | Edit Author',
            'heading'       :'Form | Edit Author',
            'post_form'     :post_form,
            'author'        :author_request,
        }
    return render(request, 'accounts/edit_author.html', context)


@login_required()
def deleteAuthorView(request, delete_id):
    Author.objects.filter(id=delete_id).delete()
    messages.success(request,'Succesfully, author has been deleted!')
    return redirect('accounts:listCategoryandAuthor')
