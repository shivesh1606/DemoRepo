# Generated by Django 4.1.2 on 2022-10-31 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ivarlab", "0003_alter_publication_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="category",
            field=models.CharField(
                choices=[
                    ("Book Chapters", "Book Chapters"),
                    ("Journal", "Journal"),
                    ("Conference", "Conference"),
                    ("Books", "Books"),
                    ("International Reports", "International Reports"),
                ],
                default="Journal",
                max_length=60,
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="category",
            field=models.CharField(
                choices=[("TEAM", "TEAM"), ("ALUMINI", "ALUMINI")],
                default="Team",
                max_length=120,
            ),
        ),
    ]
