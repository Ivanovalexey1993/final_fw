# Generated by Django 4.2.4 on 2023-09-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazin_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default='999999,99', max_digits=8),
        ),
    ]
