# Generated by Django 2.2.5 on 2019-10-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_product_rollnumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rollnumber',
            field=models.IntegerField(default=0),
        ),
    ]
