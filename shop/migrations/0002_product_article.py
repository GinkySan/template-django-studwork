# Generated by Django 5.1.4 on 2024-12-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='article',
            field=models.CharField(default='', max_length=50, verbose_name='Артикул'),
            preserve_default=False,
        ),
    ]
