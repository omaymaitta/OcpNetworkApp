# Generated by Django 4.0.6 on 2022-07-26 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameD', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameF', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameS', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameL', models.CharField(max_length=255)),
                ('departement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.departement')),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sn', models.CharField(max_length=255)),
                ('marque', models.CharField(max_length=255)),
                ('ip', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('local', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.local')),
            ],
        ),
        migrations.AddField(
            model_name='departement',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.site'),
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('durre', models.CharField(max_length=255)),
                ('equipement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.equipement')),
                ('fournisseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.fournisseur')),
            ],
        ),
    ]