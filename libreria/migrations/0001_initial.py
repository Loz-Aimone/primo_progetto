# Generated by Django 3.1.1 on 2020-12-09 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autore_AL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cognome', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Genere_AL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Libro_AL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=20)),
                ('ISBN', models.CharField(max_length=15)),
                ('Autore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libri', to='libreria.autore_al')),
                ('Genere', models.ManyToManyField(to='libreria.Genere_AL')),
            ],
        ),
    ]
