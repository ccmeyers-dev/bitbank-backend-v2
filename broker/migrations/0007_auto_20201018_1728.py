# Generated by Django 3.1 on 2020-10-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0006_auto_20201016_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(max_length=20),
        ),
    ]
