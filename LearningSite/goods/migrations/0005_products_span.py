# Generated by Django 5.1 on 2024-08-15 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_categories_description_categories_span'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='span',
            field=models.TextField(blank=True, null=True, verbose_name='Спан'),
        ),
    ]