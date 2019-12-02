# Generated by Django 2.1.4 on 2019-11-29 20:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_newplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='name',
            field=models.CharField(default='New Plan', max_length=30, verbose_name='name of plan'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date planned'),
        ),
    ]