# Generated by Django 2.2.7 on 2019-11-30 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20191201_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
