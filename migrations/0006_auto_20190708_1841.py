# Generated by Django 2.2.1 on 2019-07-08 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeappc', '0005_auto_20190708_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='cover',
        ),
        migrations.AddField(
            model_name='education',
            name='image',
            field=models.FilePathField(default='SOME STRING', path='/img'),
        ),
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.FilePathField(default='SOME STRING', path='/img'),
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='image',
            field=models.FilePathField(default='SOME STRING', path='/img'),
        ),
    ]
