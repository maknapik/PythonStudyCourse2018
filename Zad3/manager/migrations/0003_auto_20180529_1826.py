# Generated by Django 2.0.5 on 2018-05-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20180529_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='employees',
        ),
        migrations.AddField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(to='manager.Project'),
        ),
    ]