# Generated by Django 3.1 on 2020-08-15 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200815_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='articles.Tag'),
        ),
    ]
