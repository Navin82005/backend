# Generated by Django 5.0 on 2023-12-16 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0021_alter_lecturehallattadence_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Periods',
            new_name='TimeTable',
        ),
    ]
