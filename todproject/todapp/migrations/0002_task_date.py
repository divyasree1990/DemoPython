# Generated by Django 4.1.5 on 2023-02-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-04-23'),
            preserve_default=False,
        ),
    ]
