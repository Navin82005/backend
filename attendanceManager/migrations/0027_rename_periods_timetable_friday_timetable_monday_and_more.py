# Generated by Django 5.0 on 2023-12-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0026_timetable_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='periods',
            new_name='friday',
        ),
        migrations.AddField(
            model_name='timetable',
            name='monday',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='saturday',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='thursday',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='tuesday',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
        migrations.AddField(
            model_name='timetable',
            name='wednesday',
            field=models.CharField(blank=True, max_length=355, null=True),
        ),
    ]
