# Generated by Django 3.2.13 on 2022-06-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_auto_20220629_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_image',
            field=models.ImageField(blank=True, upload_to='products/% Y/% m/% d/'),
        ),
    ]