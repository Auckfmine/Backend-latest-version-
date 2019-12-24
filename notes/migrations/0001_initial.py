# Generated by Django 3.0.1 on 2019-12-24 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=' ', max_length=50)),
                ('Attitude_En_Classe', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=25, null=True)),
                ('Respect_Des_Consignes', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=25, null=True)),
                ('Autonomie', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=25, null=True)),
                ('Sociabilite', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=25, null=True)),
                ('Concentration', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=25, null=True)),
                ('Proprete', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=25, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]