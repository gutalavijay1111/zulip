# Generated by Django 3.1.7 on 2021-06-14 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0311_auto_20210613_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='position',
            field=models.CharField(default='', max_length=200),
        ),
    ]
