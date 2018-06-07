# Generated by Django 2.0.6 on 2018-06-07 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('amount', models.IntegerField()),
                ('article_numer', models.BigIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inShelf', to='pywarehouse.Article')),
            ],
        ),
        migrations.CreateModel(
            name='StorageUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storageunit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inStorageUnit', to='pywarehouse.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('warehouse_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inWarehouse', to='pywarehouse.Article')),
            ],
        ),
    ]
