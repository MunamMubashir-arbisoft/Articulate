# Generated by Django 3.1 on 2020-08-28 15:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0006_tag_click_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='clicked_by_profile',
            field=models.ManyToManyField(blank=True, related_name='tags_clicked', to=settings.AUTH_USER_MODEL),
        ),
    ]
