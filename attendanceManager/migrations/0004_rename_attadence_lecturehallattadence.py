# Generated by Django 5.0 on 2023-12-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0003_alter_attadence_date'),
        ('auth_api', '0005_alter_student_name_alter_student_registernumber_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attadence',
            new_name='LectureHallAttadence',
        ),
    ]
