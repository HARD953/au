# Generated by Django 4.1.4 on 2024-05-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_ville_donneecollectee_ville_quartier_create_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commune',
            name='ville',
            field=models.CharField(default='Abidjan', max_length=50),
        ),
    ]
