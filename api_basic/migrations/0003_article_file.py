# Generated by Django 3.2.7 on 2021-09-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0002_rename_content_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.FileField(default=-1, upload_to=''),
            preserve_default=False,
        ),
    ]
