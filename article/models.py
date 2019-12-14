from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
User = get_user_model()

class Author(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.user.username)

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.title)

class Article(models.Model):
    title           = models.CharField(max_length=255, unique=True)
    overview        = models.TextField()
    content         = RichTextUploadingField()
    timestamp       = models.DateTimeField(auto_now_add=True)
    comment_count   = models.IntegerField(default=0)
    author          = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail       = models.ImageField(null=True, blank=True)
    categories      = models.ManyToManyField(Category)
    slug            = models.SlugField(blank=True, editable=False)

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def __str__(self):
        return "{}. {}".format(self.id, self.title)
