# Generated by Django 5.0 on 2023-12-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendanceManager', '0014_remove_classsession_period_classsession_period'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturehallattadence',
            name='classSession',
        ),
        migrations.AddField(
            model_name='lecturehallattadence',
            name='h1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lecturehallattadence',
            name='h2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lecturehallattadence',
            name='h3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lecturehallattadence',
            name='h4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lecturehallattadence',
            name='h6',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lecturehallattadence',
            name='h7',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]