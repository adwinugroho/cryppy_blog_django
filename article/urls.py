from django.urls import path, re_path
from .views import detailView, categoryView
app_name = 'article'
urlpatterns = [
    #path('', indexView, name='dashboard'), #index adalah dashboard
    re_path(r'^detail/(?P<slugInput>[\w-]+)', detailView, name='detail'),
    re_path(r'^category/(?P<categoryInput>[\w-]+)', categoryView, name='category'),
]
