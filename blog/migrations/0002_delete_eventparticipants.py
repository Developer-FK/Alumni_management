# Generated by Django 3.0.6 on 2020-09-06 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EventParticipants',
        ),
    ]