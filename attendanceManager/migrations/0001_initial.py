# Generated by Django 4.2.7 on 2023-12-04 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectureHall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(blank=True, max_length=255)),
                ('names', models.ManyToManyField(related_name='student_lecture_hall', to='auth_api.student')),
            ],
        ),
    ]
