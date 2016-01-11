# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arena',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Arenaer',
            },
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('team', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Trenere',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Kamper',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('shirt_number', models.IntegerField(blank=True, null=True)),
                ('position', models.CharField(max_length=10, choices=[('K', 'Keeper'), ('B', 'Back'), ('S', 'Senter'), ('L', 'Løper')])),
            ],
            options={
                'verbose_name_plural': 'Spillere',
            },
        ),
        migrations.CreateModel(
            name='PlayerPoint',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('penalty_minutes', models.IntegerField()),
                ('match', models.ForeignKey(to='data.Match')),
                ('player', models.ForeignKey(related_name='points', to='data.Player')),
            ],
            options={
                'verbose_name_plural': 'Poeng',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('score_hometeam', models.IntegerField()),
                ('score_awayteam', models.IntegerField()),
                ('match', models.OneToOneField(to='data.Match')),
            ],
            options={
                'verbose_name_plural': 'Resultater',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Lag',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='matches',
            field=models.ManyToManyField(through='data.PlayerPoint', to='data.Match'),
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='data.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(related_name='away_matches', to='data.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(related_name='home_matches', to='data.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='venue',
            field=models.ForeignKey(to='data.Arena'),
        ),
        migrations.AlterUniqueTogether(
            name='playerpoint',
            unique_together=set([('player', 'match')]),
        ),
    ]
