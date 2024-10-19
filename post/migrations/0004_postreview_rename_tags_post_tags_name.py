# Generated by Django 5.1.1 on 2024-09-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='tags',
            new_name='tags_name',
        ),
    ]