# Generated by Django 2.1.4 on 2019-02-28 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter Stock Name', max_length=200)),
                ('description', models.TextField(help_text='Enter Product Description')),
                ('unitCost', models.FloatField(help_text='Enter Stock Unit Cost')),
                ('unit', models.CharField(help_text='Enter Stock Unit ', max_length=10)),
                ('quantity', models.FloatField(help_text='Enter Stock Quantity')),
                ('minQuantity', models.FloatField(help_text='Enter Stock Min Quantity')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitCost', models.FloatField(help_text='Enter Stock Unit Cost')),
                ('quantity', models.FloatField(help_text='Enter Stock Quantity')),
                ('date', models.DateField(blank=True, null=True)),
                ('reason', models.CharField(blank=True, choices=[('ns', 'New Stock'), ('ur', 'Usable Return'), ('nr', 'Unusable Return')], default='ns', help_text='Reason for transaction', max_length=2)),
                ('Stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Stocks')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter User Name', max_length=200)),
                ('description', models.TextField(help_text='Enter Family Description')),
            ],
        ),
        migrations.AddField(
            model_name='stocks',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
