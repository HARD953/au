# Generated by Django 4.1.4 on 2023-11-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donneecollectee',
            name='image_support',
            field=models.ImageField(blank=True, null=True, upload_to='collecte_images/'),
        ),
    ]
