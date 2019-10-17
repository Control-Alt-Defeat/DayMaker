# Generated by Django 2.2.5 on 2019-09-26 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0004_auto_20190926_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventfinder',
            name='loc_type',
            field=models.CharField(choices=[('1', 'Mexican Food'), ('2', 'Ice Cream'), ('3', 'Coffee Shop'), ('4', 'Seafood'), ('5', 'Other Restaurants')], max_length=1, verbose_name='Location Type'),
        ),
    ]