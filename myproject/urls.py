from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import indexView, aboutView

urlpatterns = [
    path('akuadmin/', admin.site.urls),
    path('accounts/',include('accounts.urls', namespace="accounts")),
    path('article/',include('article.urls', namespace="article")),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('',indexView, name='home'),
    path('about/', aboutView, name='about')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
INI DOKUMENTASI.
mohon dibaca!
+static dan seterusnya adalah konfigurasi untuk memanggil dan menyimpan media
media apa? media seperti gambar yang diupload atau media CKEditor
JANGAN LUPA IMPORT LIBRARYNYA YAITU django.conf.urls.static import static
jadi cuman ada 2 halaman di myproject yang pertama HOME dan yang kedua ABOUT
"""