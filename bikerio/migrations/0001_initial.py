# Generated by Django 4.2.1 on 2023-05-15 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gbfs_href', models.URLField()),
                ('href', models.CharField(max_length=100)),
                ('network_id', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('name', models.CharField(max_length=100)),
                ('company', models.ManyToManyField(to='bikerio.company')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty_slots', models.IntegerField()),
                ('free_bikes', models.IntegerField()),
                ('station_id', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('name', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stations', to='bikerio.network')),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('station', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='bikerio.station')),
                ('address', models.CharField(max_length=100)),
                ('altitude', models.IntegerField(null=True)),
                ('ebikes', models.IntegerField()),
                ('has_ebikes', models.BooleanField()),
                ('last_updated', models.IntegerField()),
                ('normal_bikes', models.IntegerField()),
                ('payment_terminal', models.BooleanField()),
                ('renting', models.BooleanField()),
                ('returning', models.BooleanField()),
                ('slots', models.IntegerField()),
                ('uid', models.CharField(max_length=100)),
                ('payment', models.ManyToManyField(to='bikerio.payment')),
            ],
        ),
    ]
