# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0003_auto_20170918_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('Autores', models.ManyToManyField(null=True, related_name='autores', to='projeto.Autor')),
            ],
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projeto.Evento')),
                ('sn', models.CharField(max_length=20)),
            ],
            bases=('projeto.evento',),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventocientifico', to='projeto.EventoCientifico'),
        ),
    ]
