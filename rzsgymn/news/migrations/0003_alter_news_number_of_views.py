# Generated by Django 4.1 on 2022-08-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_number_of_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='number_of_views',
            field=models.PositiveIntegerField(default=0, verbose_name='Кількість переглядів'),
        ),
    ]