# Generated by Django 4.0.5 on 2022-08-08 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0008_alter_archivedocument_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivedocument',
            name='color',
        ),
        migrations.RemoveField(
            model_name='archivedocument',
            name='image_content',
        ),
        migrations.RemoveField(
            model_name='archivedocument',
            name='medium',
        ),
        migrations.RemoveField(
            model_name='archivedocument',
            name='record_type',
        ),
        migrations.RemoveField(
            model_name='document',
            name='language',
        ),
        migrations.AddField(
            model_name='photograph',
            name='color',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='photograph',
            name='creator',
            field=models.TextField(blank=True, default='Lois, Lauren, and Julia', max_length=50),
        ),
        migrations.AddField(
            model_name='photograph',
            name='image_content',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='photograph',
            name='language',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='photograph',
            name='medium',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='photograph',
            name='record_type',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
