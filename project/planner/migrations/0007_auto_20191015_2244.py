# Generated by Django 2.2.5 on 2019-10-16 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0006_auto_20191015_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventfinder',
            name='end_time',
            field=models.TimeField(null=True, verbose_name='end time of event'),
        ),
        migrations.AddField(
            model_name='eventfinder',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='start time of event'),
        ),
        migrations.AlterField(
            model_name='searchresult',
            name='chosen',
            field=models.IntegerField(default=0),
        ),
    ]
