# Generated by Django 2.2.5 on 2019-11-19 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0014_auto_20191119_0955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventfinder',
            old_name='location',
            new_name='address',
        ),
    ]