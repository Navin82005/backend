# Generated by Django 5.0 on 2024-01-31 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0008_student_lecturehall'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='userDob',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='userMobile',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
