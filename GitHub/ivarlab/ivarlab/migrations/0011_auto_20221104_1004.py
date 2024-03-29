# Generated by Django 3.2.9 on 2022-11-04 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivarlab', '0010_auto_20221104_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.CharField(choices=[('Conference', 'Conference'), ('International Reports', 'International Reports'), ('Book Chapters', 'Book Chapters'), ('Journal', 'Journal'), ('Books', 'Books')], default='Journal', max_length=60),
        ),
        migrations.AlterField(
            model_name='team',
            name='category',
            field=models.CharField(choices=[('ALUMINI', 'ALUMINI'), ('TEAM', 'TEAM')], default='Team', max_length=120),
        ),
    ]
