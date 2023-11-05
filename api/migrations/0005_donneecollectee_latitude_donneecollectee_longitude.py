# Generated by Django 4.1.4 on 2023-11-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_donneecollectee_odp_value_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donneecollectee',
            name='latitude',
            field=models.FloatField(blank=True, default=4.1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donneecollectee',
            name='longitude',
            field=models.FloatField(blank=True, default=3.1),
            preserve_default=False,
        ),
    ]