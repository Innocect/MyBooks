# Generated by Django 2.2.5 on 2019-10-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
