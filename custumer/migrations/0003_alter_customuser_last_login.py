# Generated by Django 4.1.4 on 2024-06-23 19:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0002_alter_customuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 23, 19, 38, 2, 148784, tzinfo=datetime.timezone.utc)),
        ),
    ]
