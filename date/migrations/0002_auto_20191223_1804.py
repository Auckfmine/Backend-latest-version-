# Generated by Django 3.0.1 on 2019-12-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('date', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='child',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='date',
            name='data1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='date',
            name='father',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
