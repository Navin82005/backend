# Generated by Django 4.2.7 on 2023-11-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('password', models.CharField(max_length=6255)),
            ],
        ),
    ]
