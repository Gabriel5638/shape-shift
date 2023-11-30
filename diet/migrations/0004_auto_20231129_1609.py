# Generated by Django 3.2.21 on 2023-11-29 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0003_auto_20231129_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealjournalentry',
            name='date_time',
        ),
        migrations.AddField(
            model_name='mealjournalentry',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mealjournalentry',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]