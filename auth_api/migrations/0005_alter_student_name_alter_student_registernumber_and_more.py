# Generated by Django 4.2.7 on 2023-12-04 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0004_student_registernumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='registerNumber',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='student',
            name='rollNumber',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
