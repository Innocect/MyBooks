# Generated by Django 2.2.5 on 2019-10-05 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_product_paid_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rollnumber',
            field=models.IntegerField(default=0),
        ),
    ]
