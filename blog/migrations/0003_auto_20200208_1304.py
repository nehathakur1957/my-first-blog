# Generated by Django 3.0.2 on 2020-02-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200208_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='document',
            field=models.ImageField(blank=True, upload_to='documents/'),
        ),
    ]
