# Generated by Django 4.2 on 2023-04-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event_management_application", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="email_sent",
            field=models.BooleanField(default=False),
        ),
    ]
