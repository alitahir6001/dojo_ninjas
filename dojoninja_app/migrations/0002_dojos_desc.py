# Generated by Django 2.2.4 on 2020-12-13 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojoninja_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='dojodescription'),
            preserve_default=False,
        ),
    ]
