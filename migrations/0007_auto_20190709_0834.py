# Generated by Django 2.2.1 on 2019-07-09 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resumeappc', '0006_auto_20190708_1841'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='image',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='image',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='image',
        ),
    ]
