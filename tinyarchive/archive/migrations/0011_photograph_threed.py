# Generated by Django 4.0.5 on 2022-08-09 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0010_remove_photograph_creator_archivedocument_creator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='threed',
            field=models.URLField(blank='True', max_length=500),
        ),
    ]
