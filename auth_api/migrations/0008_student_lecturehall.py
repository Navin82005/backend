# Generated by Django 5.0 on 2024-01-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0007_staff_lecturehall'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='lectureHall',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
