# Generated by Django 2.2.7 on 2019-11-26 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de création')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('name', models.CharField(max_length=100, verbose_name='Note')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
        migrations.AddField(
            model_name='call',
            name='note',
            field=models.CharField(default=0, max_length=100, verbose_name='CallNote'),
            preserve_default=False,
        ),
    ]
