from django.contrib import admin
from .models import Article,Author,Category
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'timestamp',
    ]
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)