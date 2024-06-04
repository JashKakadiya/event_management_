# Generated by Django 5.0.6 on 2024-06-04 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management_application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='location_id',
        ),
        migrations.AlterField(
            model_name='tickets',
            name='ticket_type',
            field=models.CharField(blank=True, choices=[('VIP', 'VIP'), ('BASE', 'BASE')], max_length=50),
        ),
    ]