# Generated by Django 3.2 on 2021-04-23 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=400)),
                ('status', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'annoncements',
            },
        ),
    ]
