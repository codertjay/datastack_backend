# Generated by Django 3.2.8 on 2021-10-31 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
