# Generated by Django 2.2.7 on 2019-11-27 16:07

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20191127_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='overview',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
