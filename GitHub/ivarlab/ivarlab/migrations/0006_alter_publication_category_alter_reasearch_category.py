# Generated by Django 4.1.2 on 2022-10-31 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ivarlab", "0005_reasearch_delete_view_count_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="category",
            field=models.CharField(
                choices=[
                    ("Books", "Books"),
                    ("Journal", "Journal"),
                    ("International Reports", "International Reports"),
                    ("Book Chapters", "Book Chapters"),
                    ("Conference", "Conference"),
                ],
                default="Journal",
                max_length=60,
            ),
        ),
        migrations.AlterField(
            model_name="reasearch",
            name="category",
            field=models.CharField(
                choices=[
                    ("Invited Talks", "Invited Talks"),
                    ("Conference Presentation", "Conference Presentation"),
                    ("Editorial Boards", "Editorial Boards"),
                ],
                default="Invited Talks",
                max_length=60,
            ),
        ),
    ]