# Generated by Django 4.1.4 on 2024-05-07 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custumer', '0003_alter_customuser_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 7, 10, 20, 31, 521143, tzinfo=datetime.timezone.utc)),
        ),
    ]
