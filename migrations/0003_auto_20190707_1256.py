# Generated by Django 2.2.1 on 2019-07-07 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeappc', '0002_auto_20190701_1850'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonalInfo',
        ),
        migrations.AlterField(
            model_name='education',
            name='School_attended',
            field=models.CharField(max_length=100),
        ),
    ]
