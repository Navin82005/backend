# Generated by Django 5.0 on 2024-01-31 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0009_student_userdob_student_usermobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='userDob',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='staff',
            name='userMobile',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]