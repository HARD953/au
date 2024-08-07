# Generated by Django 4.1.4 on 2024-06-20 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canal', models.CharField(max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(default='Abidjan', max_length=50)),
                ('commune', models.CharField(default='Abidjan', max_length=50)),
                ('tauxODP', models.CharField(default='6', max_length=50)),
                ('tauxTSP', models.CharField(default='7', max_length=50)),
                ('tauxAP', models.CharField(max_length=50)),
                ('tauxAPA', models.CharField(max_length=50)),
                ('tauxAPT', models.CharField(max_length=50)),
                ('tauxAE', models.CharField(max_length=50)),
                ('tauxAEA', models.CharField(max_length=50)),
                ('tauxAET', models.CharField(max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DonneeCollectee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entreprise', models.CharField(blank=True, max_length=50)),
                ('Marque', models.CharField(blank=True, max_length=50)),
                ('ville', models.CharField(blank=True, max_length=50)),
                ('commune', models.CharField(blank=True, max_length=50)),
                ('quartier', models.CharField(blank=True, max_length=50)),
                ('type_support', models.CharField(blank=True, max_length=50)),
                ('surface', models.CharField(blank=True, max_length=50)),
                ('surfaceODP', models.CharField(blank=True, max_length=50)),
                ('canal', models.CharField(blank=True, max_length=50)),
                ('etat_support', models.CharField(blank=True, max_length=50)),
                ('typesite', models.CharField(blank=True, max_length=50)),
                ('visibilite', models.CharField(blank=True, max_length=50)),
                ('description', models.CharField(blank=True, max_length=50)),
                ('observation', models.CharField(blank=True, max_length=50)),
                ('date_collecte', models.DateTimeField(auto_now_add=True)),
                ('image_support', models.ImageField(blank=True, null=True, upload_to='collecte_images/')),
                ('signature', models.ImageField(blank=True, null=True, upload_to='collecte_images/')),
                ('nom1', models.CharField(blank=True, max_length=50)),
                ('nom2', models.CharField(blank=True, max_length=50)),
                ('nom3', models.CharField(blank=True, max_length=50)),
                ('duree', models.CharField(blank=True, max_length=50)),
                ('anciennete', models.BooleanField(blank=True, default=False)),
                ('TSP', models.CharField(blank=True, default=12, max_length=50)),
                ('ODP', models.BooleanField(blank=True, default=False)),
                ('AP', models.BooleanField(blank=True, default=False)),
                ('APA', models.BooleanField(blank=True, default=False)),
                ('APT', models.BooleanField(blank=True, default=False)),
                ('AE', models.BooleanField(blank=True, default=False)),
                ('AEA', models.BooleanField(blank=True, default=False)),
                ('AET', models.BooleanField(blank=True, default=False)),
                ('ODP_value', models.CharField(blank=True, default=1, max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField(blank=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Etat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat', models.CharField(max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque', models.CharField(max_length=50)),
                ('surface', models.CharField(blank=True, max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quartier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commune', models.CharField(default='Abidjan', max_length=50)),
                ('quartier', models.CharField(default='Rue 12', max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SupportPublicitaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_support', models.CharField(max_length=50)),
                ('surface', models.CharField(max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taux',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TTAP', models.CharField(max_length=50)),
                ('TTPAT', models.CharField(max_length=50)),
                ('TAE', models.CharField(max_length=50)),
                ('TAEAT', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(default='Abidjan', max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visibilite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visibilite', models.CharField(max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
