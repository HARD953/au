# Generated by Django 4.1.4 on 2023-12-14 22:26

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
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 14, 22, 26, 2, 100116, tzinfo=datetime.timezone.utc)),
        ),
    ]
