# Generated by Django 5.0 on 2023-12-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0015_remove_lecturehallattadence_classsession_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturehallattadence',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
