# Generated by Django 4.1.6 on 2023-02-11 15:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0005_alter_project_options_alter_review_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="project",
            options={"ordering": ["-vote_ratio", "-vote_total", "title"]},
        ),
    ]