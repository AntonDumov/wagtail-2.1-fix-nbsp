# Generated by Django 1.9.4 on 2016-03-29 04:28
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippetstests", "0002_searchablesnippet"),
    ]

    operations = [
        migrations.CreateModel(
            name="FancySnippet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StandardSnippet",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=255)),
            ],
        ),
    ]
