# Generated by Django 2.1.4 on 2019-03-02 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20190302_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='stock',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Stocks'),
        ),
    ]
