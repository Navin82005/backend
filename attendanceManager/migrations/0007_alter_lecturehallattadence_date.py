# Generated by Django 5.0 on 2023-12-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0006_lecturehallattadence_ispresent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturehallattadence',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
