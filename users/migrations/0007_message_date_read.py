# Generated by Django 4.1.6 on 2023-02-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_rename_name_message_sender_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="date_read",
            field=models.DateTimeField(null=True),
        ),
    ]
