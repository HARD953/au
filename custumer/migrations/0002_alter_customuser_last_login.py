# Generated by Django 4.1.4 on 2023-10-08 22:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 22, 9, 52, 115189, tzinfo=datetime.timezone.utc)),
        ),
    ]
