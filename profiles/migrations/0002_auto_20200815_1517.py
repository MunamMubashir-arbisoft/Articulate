# Generated by Django 3.1 on 2020-08-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200815_1517'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='followed_profiles',
            field=models.ManyToManyField(blank=True, null=True, related_name='_profile_followed_profiles_+', to='profiles.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='starred_articles',
            field=models.ManyToManyField(blank=True, null=True, related_name='starred', to='articles.Article'),
        ),
    ]