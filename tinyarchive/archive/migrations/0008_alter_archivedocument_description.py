# Generated by Django 4.0.5 on 2022-08-06 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0007_alter_archivedocument_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivedocument',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
