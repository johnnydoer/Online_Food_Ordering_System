# Generated by Django 2.1.2 on 2018-11-28 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_auto_20181127_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='GrandTotal',
            field=models.IntegerField(default=0),
        ),
    ]