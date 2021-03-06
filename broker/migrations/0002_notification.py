# Generated by Django 3.1 on 2020-10-14 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('message', models.TextField(max_length=500)),
                ('read', models.BooleanField(default=False)),
                ('portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='broker.portfolio')),
            ],
        ),
    ]
