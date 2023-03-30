# Generated by Django 4.1.7 on 2023-03-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='emp_dob',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='DOB'),
        ),
        migrations.AddField(
            model_name='contact',
            name='emp_gender',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='gender'),
        ),
    ]
