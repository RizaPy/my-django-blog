# Generated by Django 5.1.1 on 2024-10-12 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0009_rename_content_postreview_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]