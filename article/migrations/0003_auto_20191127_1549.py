# Generated by Django 2.2.7 on 2019-11-27 15:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='overview',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
