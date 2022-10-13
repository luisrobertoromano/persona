# Generated by Django 3.2 on 2022-08-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de la oficina')),
                ('nombre_corto', models.CharField(max_length=50, verbose_name='Nombre corto')),
            ],
            options={
                'verbose_name': 'Oficina',
                'verbose_name_plural': 'Oficinas',
            },
        ),
    ]