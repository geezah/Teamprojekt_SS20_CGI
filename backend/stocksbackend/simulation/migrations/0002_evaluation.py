# Generated by Django 3.0.6 on 2020-08-29 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('score', models.FloatField()),
                ('simulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulation.Simulation')),
            ],
        ),
    ]
