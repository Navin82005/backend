# Generated by Django 5.0 on 2023-12-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0029_timetable_hour'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timetable',
            options={'ordering': ['day', 'hour']},
        ),
        migrations.AlterField(
            model_name='timetable',
            name='Class',
            field=models.ManyToManyField(to='attendanceManager.lecturehall'),
        ),
    ]
