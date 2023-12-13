# Generated by Django 5.0 on 2023-12-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0013_lecturehallattadence_classsession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classsession',
            name='period',
        ),
        migrations.AddField(
            model_name='classsession',
            name='period',
            field=models.ManyToManyField(to='attendanceManager.periods'),
        ),
    ]
