# Generated by Django 3.1 on 2020-09-30 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='referrer',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
