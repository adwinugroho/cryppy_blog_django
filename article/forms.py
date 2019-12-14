from django import forms
from ckeditor.widgets import CKEditorWidget
from django.forms.widgets import FileInput, SelectMultiple, CheckboxSelectMultiple

from .models import Article,Author,Category

class ArticleForm(forms.ModelForm):
    class Meta:
        model   = Article
        fields  = [
            'title',
            'overview',
            'content',
            'author',
            'thumbnail',
            'categories',
        ]

        widgets = {
            'title':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Enter article title',
                }
            ),
            'overview':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Enter article overview',
                }
            ),
            'author':forms.HiddenInput(
                attrs = {
                    'class':'form-control',
                }
            ),
            'categories': SelectMultiple(
                attrs = {
                    'class':'form-control',
                    'data-height':'100%',
                }
            ),
            'thumbnail':FileInput(
                attrs = {
                    'class':'form-control',
                }
            ),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model   = Category
        fields  = [
            'title',
        ]
        widgets = {
            'title':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Enter new category',
                }
            ),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model   = Author
        fields  = [
            'user',
        ]
        widgets = {
            'user':forms.Select(
                attrs = {
                    'class':'form-control',
                }
            ),
        }