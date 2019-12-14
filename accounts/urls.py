from django.urls import path, re_path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    dashboardView, 
    editProfileView,
    changePasswordView,
    registerView, 
    createCategoryView,
    createAuthorView,
    listCategoryandAuthorView,
    editCategoryView,
    editAuthorView,
    deleteCategoryView,
    deleteAuthorView,
    deleteConfirmAuthorView,
    deleteConfirmCategoryView,
)
from article.views import createView, editView, deleteView, deleteConfirmArticleView
from .forms import UserLoginForm, EditPasswordForm
from django.contrib.auth.forms import PasswordChangeForm
app_name = 'accounts'
urlpatterns = [
    #ACCOUNTS
    path('dashboard/', dashboardView, name='dashboard'),
    path('dashboard/profile/', editProfileView, name='profile'),
    path('dashboard/password/', changePasswordView, name='change-password'),
    path('login/', LoginView.as_view(
        template_name='accounts/login.html', 
        authentication_form=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(
        next_page='accounts:dashboard'), name='logout'),
    path('register/', registerView, name='register'),

    #ARTICLES
    path('dashboard/article/create/', createView, name='createArticle'),
    re_path(r'^dashboard/article/update/(?P<update_id>[0-9]+)$', editView, name='editArticle'),
    re_path(r'^dashboard/article/delete/(?P<delete_id>[0-9]+)$', deleteView, name='deleteArticle'),
    re_path(r'^dashboard/article/detail/delete/(?P<delete_id>[0-9]+)$', deleteConfirmArticleView, name='deleteConfirmArticle'),

    #STAFF ONLY MANAGE THIS PAGE
    path('dashboard/manage/author/create', createAuthorView, name='createAuthor'),
    path('dashboard/manage/category/create', createCategoryView, name='createCategory'),
    path('dashboard/manage/list', listCategoryandAuthorView, name='listCategoryandAuthor'),
    re_path(r'^dashboard/manage/author/delete/(?P<delete_id>[0-9]+)$', deleteConfirmAuthorView, name='deleteConfirmAuthor'),
    re_path(r'^dashboard/manage/category/delete/(?P<delete_id>[0-9]+)$', deleteConfirmCategoryView, name='deleteConfirmCategory'),
    re_path(r'^dashboard/category/update/(?P<update_id>[0-9]+)$', editCategoryView, name='editCategory'),
    re_path(r'^dashboard/category/delete/(?P<delete_id>[0-9]+)$', deleteCategoryView, name='deleteCategory'),
    re_path(r'^dashboard/author/update/(?P<update_id>[0-9]+)$', editAuthorView, name='editAuthor'),
    re_path(r'^dashboard/author/delete/(?P<delete_id>[0-9]+)$', deleteAuthorView, name='deleteAuthor'),
]
