# Generated by Django 2.1.4 on 2019-03-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.IntegerField(default=0, help_text='Enter Stock Quantity'),
        ),
    ]