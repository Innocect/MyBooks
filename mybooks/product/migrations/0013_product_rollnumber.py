# Generated by Django 2.2.5 on 2019-10-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20191004_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rollnumber',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
