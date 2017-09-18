# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projeto.Pessoa')),
                ('cpf', models.CharField(max_length=11)),
            ],
            bases=('projeto.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJurifica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='projeto.Pessoa')),
                ('cnpj', models.CharField(max_length=13)),
                ('razaoSocial', models.CharField(max_length=50)),
            ],
            bases=('projeto.pessoa',),
        ),
        migrations.AlterField(
            model_name='evento',
            name='dataEHoraDeInicio',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
