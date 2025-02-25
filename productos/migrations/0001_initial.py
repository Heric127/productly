# Generated by Django 5.1.3 on 2024-11-30 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('puntaje', models.FloatField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.categoria')),
            ],
        ),
    ]
