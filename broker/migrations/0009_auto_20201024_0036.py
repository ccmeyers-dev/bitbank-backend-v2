# Generated by Django 3.1 on 2020-10-23 23:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0008_card_ssn'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deposit',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterModelOptions(
            name='trade',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterModelOptions(
            name='withdrawal',
            options={'ordering': ('-date_created',)},
        ),
        migrations.AlterField(
            model_name='deposit',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='trade',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.FloatField(editable=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='duration',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='portfolio',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='broker.portfolio'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='profit',
            field=models.FloatField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(blank=True, editable=False, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='broker.wallet'),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
