# Generated by Django 2.1.4 on 2019-03-02 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20190303_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocks',
            name='quantity',
            field=models.IntegerField(default=0.0, help_text='Enter Stock Quantity'),
        ),
    ]
