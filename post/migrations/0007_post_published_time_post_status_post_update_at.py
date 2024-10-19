# Generated by Django 5.1.1 on 2024-09-30 13:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('Draft', 'DR'), ('Published', 'PB')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
